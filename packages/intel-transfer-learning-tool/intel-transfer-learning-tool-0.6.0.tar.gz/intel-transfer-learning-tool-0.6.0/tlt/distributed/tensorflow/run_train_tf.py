#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2023 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# SPDX-License-Identifier: Apache-2.0
#

import os
import tempfile
import argparse

import tensorflow as tf
import tensorflow_datasets as tfds

from filelock import FileLock

from tlt.distributed.tensorflow.utils.tf_distributed_util import (
    DistributedTF,
    DistributedTrainingArguments
)
from tlt.models.model_factory import get_supported_models


if __name__ == '__main__':

    dist_tf = DistributedTF()

    hvd_lock_file = os.path.join(tempfile.gettempdir(), '.horovod_lock')
    default_data_dir = os.path.join(tempfile.gettempdir(), 'data')
    default_output_dir = os.path.join(tempfile.gettempdir(), 'output')

    # Create directories "/tmp/data" and "/tmp/output" if they don't exist
    with FileLock(hvd_lock_file):
        for d in [default_data_dir, default_output_dir]:
            if not os.path.exists(d):
                os.makedirs(d)

    def directory_path(path):
        if os.path.isdir(path):
            return path
        else:
            raise argparse.ArgumentTypeError("'{}' is not a valid directory path.".format(path))

    print("******Distributed Training*****")

    description = 'Distributed training with TensorFlow.'

    parser = argparse.ArgumentParser(description=description)

    parser.add_argument('--use-case', '--use_case', type=str, required=True, choices=['image_classification',
                        'text_classification'], help='Use case (image_classification|text_classification)')
    parser.add_argument('--epochs', type=int, required=False, default=1, help='Total epochs to train the model')
    parser.add_argument('--batch_size', type=int, required=False, default=128,
                        help='Global batch size to distribute data (default: 128)')
    parser.add_argument("--batch_denom", type=int, required=False, default=1,
                        help="Batch denominator to be used to divide global batch size (default: 1)")
    parser.add_argument('--shuffle', action='store_true', required=False, help="Shuffle dataset while training")
    parser.add_argument('--scaling', type=str, required=False, default='weak', choices=['weak', 'strong'],
                        help='Weak or Strong scaling. For weak scaling, lr is scaled by a factor of '
                        'sqrt(batch_size/batch_denom) and uses global batch size for all the processes. For '
                        'strong scaling, lr is scaled by world size and divides global batch size by world size '
                        '(default: weak)')
    parser.add_argument('--tlt_saved_objects_dir', type=directory_path, required=False, help='Path to TLT saved '
                        'distributed objects. The path must be accessible to all the nodes. For example: mounted '
                        'NFS drive. This arg is helpful when using TLT API/CLI. See DistributedTF.load_saved_objects()'
                        ' for more information.')
    parser.add_argument('--max_seq_length', type=int, default=128,
                        help='Maximum sequence length that the model will be used with')
    parser.add_argument('--dataset-dir', '--dataset_dir', type=directory_path, default=default_data_dir,
                        help="Path to dataset directory to save/load tfds dataset. This arg is helpful if you "
                        "plan to use this as a stand-alone script. Custom dataset is not supported yet!")
    parser.add_argument('--output-dir', '--output_dir', type=directory_path, default=default_output_dir,
                        help="Path to save the trained model and store logs. This arg is helpful if you "
                        "plan to use this as a stand-alone script")
    parser.add_argument('--dataset-name', '--dataset_name', type=str, default=None,
                        help="Dataset name to load from tfds. This arg is helpful if you "
                        "plan to use this as a stand-alone script. Custom dataset is not supported yet!")
    parser.add_argument('--model-name', '--model_name', type=str, default=None,
                        help="TensorFlow image classification model name (or) Huggingface hub model name for text "
                        "classification. This arg is helpful if you plan to use this as a stand-alone script.")
    parser.add_argument('--k8', action='store_true', required=False,
                        help="Use this flag when running on a Kubernetes cluster to differentiate with the "
                        "dataset download logic on bare metal.")

    args = parser.parse_args()

    model = None
    optimizer, loss = None, None
    train_data, train_labels = None, None
    val_data, val_labels = None, None

    if args.tlt_saved_objects_dir is not None:
        model, optimizer, loss, train_data, val_data = dist_tf.load_saved_objects(args.tlt_saved_objects_dir)
    else:
        supported_models = get_supported_models('tensorflow', args.use_case)
        if args.dataset_name is None:
            raise ValueError("Please provide a dataset name to load from tfds "
                             "using --dataset-name")
        if args.model_name is None or args.model_name not in supported_models[args.use_case].keys():
            raise ValueError("Please provide/modify TensorFlow Hub's model name (or) "
                             "Huggingface hub model name. Supported models for {} are:\n {}".format(
                                 args.use_case, list(supported_models[args.use_case].keys())))

        if args.k8:
            # Change the lock file to a location shared by PVC and visible to all k8 workers.
            hvd_lock_file = os.path.join(args.dataset_dir, '.horovod_lock')

        with FileLock(hvd_lock_file):
            train_data, data_info = tfds.load(args.dataset_name, data_dir=args.dataset_dir, split='train',
                                              as_supervised=True, with_info=True)
            val_data = tfds.load(args.dataset_name, data_dir=args.dataset_dir, split='test', as_supervised=True)
        os.remove(hvd_lock_file)
        num_classes = data_info.features['label'].num_classes

        if args.use_case == 'image_classification':
            model_url = supported_models['image_classification'][args.model_name]['tensorflow']['feature_vector']
            image_size = supported_models['image_classification'][args.model_name]['tensorflow']['image_size']
            input_shape = (image_size, image_size, 3)

            def preprocess_image(image, label):
                image = tf.image.convert_image_dtype(image, tf.float32)
                image = tf.image.resize_with_pad(image, image_size, image_size)
                return (image, label)

            train_data = dist_tf.prepare_dataset(train_data, args.use_case, args.batch_size, args.scaling,
                                                 map_func=preprocess_image)
            val_data = dist_tf.prepare_dataset(val_data, args.use_case, args.batch_size, args.scaling,
                                               map_func=preprocess_image)

            model = dist_tf.prepare_model(model_url, args.use_case, input_shape, num_classes)

        elif args.use_case == 'text_classification':
            input_shape = (args.max_seq_length,)
            from transformers import BertTokenizer
            hf_bert_tokenizer = BertTokenizer.from_pretrained(args.model_name)

            train_data = dist_tf.prepare_dataset(
                train_data, args.use_case, args.batch_size, args.scaling,
                max_seq_length=args.max_seq_length, hf_bert_tokenizer=hf_bert_tokenizer
            )
            val_data = dist_tf.prepare_dataset(val_data, args.use_case, args.batch_size, args.scaling,
                                               max_seq_length=args.max_seq_length, hf_bert_tokenizer=hf_bert_tokenizer)
            model = dist_tf.prepare_model(args.model_name, args.use_case, input_shape, num_classes)

        optimizer = tf.keras.optimizers.Adam()
        loss = tf.keras.losses.BinaryCrossentropy(from_logits=True) if num_classes == 2 else \
            tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

    training_args = DistributedTrainingArguments(
        use_case=args.use_case,
        model=model,
        optimizer=optimizer,
        loss=loss,
        train_data=train_data,
        val_data=val_data,
        epochs=args.epochs,
        scaling=args.scaling,
        batch_size=args.batch_size,
        batch_denom=args.batch_denom,
        shuffle=args.shuffle,
        max_seq_length=args.max_seq_length,
        hf_bert_tokenizer=args.model_name if args.tlt_saved_objects_dir is not None and
        args.use_case == 'text_classification' else None
    )

    dist_tf.launch_distributed_job(training_args)
