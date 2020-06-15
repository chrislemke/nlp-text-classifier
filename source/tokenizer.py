# -*- coding: utf-8 -*-

import os
import re
import json
import sys
from tensorflow.keras.preprocessing import text
import dataset_processing as dp
import tensorflow_datasets as tfds
from dataset_processing import combined_dataset
import nltk

OUTPUT_TOKEN_PATH = os.path.abspath(
    __file__ + f"/../../output/tokenizer/tokens")


def tfds_tokens():
    tokenizer = tfds.features.text.Tokenizer(alphanum_only=True)

    vocabulary_set = set()
    sentences_count = 0

    for sentence_tensor, _ in dp.combined_dataset():
        sentences_count += 1
        some_tokens = tokenizer.tokenize(sentence_tensor.numpy())

        lower_tokens = []
        for token in some_tokens:
            lower_tokens.append(token)

        vocabulary_set.update(lower_tokens)

    print(
        f'Found {sentences_count} sentences from {len(dp.FILE_NAMES)} author(s).')
    print(f'Found {len(vocabulary_set)} unique vocabularies.')
    return vocabulary_set


def nltk_tokens():
    vocabulary_set = set()
    sentences_count = 0

    for sentence_tensor, _ in dp.combined_dataset():
        sentences_count += 1

        sentence = str(sentence_tensor.numpy())
        sentence = sentence.replace("b'", '', 1)
        tokenized_words = nltk.word_tokenize(
            sentence, language='german')
        vocabulary_set.update(tokenized_words)

    print(
        f'Found {sentences_count} sentences from {len(dp.FILE_NAMES)} file(s).')
    print(f'Found {len(vocabulary_set)} unique vocabularies.')
    return vocabulary_set