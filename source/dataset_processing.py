# -*- coding: utf-8 -*-

import re
import os
import tensorflow as tf
import nltk

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
nltk.download('punkt')

FILE_NAMES = [
    'phil_epoch_antike_merged_file.txt', 'phil_epoch_idealismus_merged_file.txt', 'phil_epoch_neuzeit_merged_file.txt']

PROCESSED_PATH = os.path.abspath(
    __file__ + f"/../../input/processed/")
BUFFER_SIZE = 61800


def labeler(example, index):
    return example, tf.cast(index, tf.int64)


def combine_datasets(datasets):
    all_labeled_data = datasets[0]
    for labeled_dataset in datasets[1:]:
        all_labeled_data = all_labeled_data.concatenate(labeled_dataset)

    all_labeled_data = all_labeled_data.shuffle(
        BUFFER_SIZE, reshuffle_each_iteration=False)
    return all_labeled_data


def datasets():
    all_labeled_datasets = []
    for index, file_name in enumerate(FILE_NAMES):
        path = os.path.join(PROCESSED_PATH, file_name)

        tensors = []

        with open(path, encoding='UTF-8') as file:
            text = file.read()
            sentences = nltk.sent_tokenize(text, language='german')

            for sentence in sentences:
                if ' ' in sentence == False:
                    continue
                if len(sentence) <= 20:
                    continue
                tensors.append(tf.constant(sentence))

            dataset = tf.data.Dataset.from_tensor_slices(tensors)

            labeled_dataset = dataset.map(lambda ex: labeler(ex, index))
            all_labeled_datasets.append(labeled_dataset)
            print(f"Created dataset for {file_name} with index: {index}.")

    return all_labeled_datasets


def combined_dataset():
    return combine_datasets(datasets())
