import tensorflow_datasets as tfds
import tensorflow as tf
import tokenizer as tok
import dataset_processing as ds
import os
from dataset_processing import combined_dataset

OUTPUT_ENCODER_PATH = os.path.abspath(
    __file__ + f"/../../output/encoding/encoded")

dataset = combined_dataset()


def encode_text(text_tensor, label):
    encoded_text = encoder.encode(text_tensor.numpy())
    return encoded_text, label


def encode_map(text, label):
    encoded_text, label = tf.py_function(encode_text,
                                         inp=[text, label],
                                         Tout=(tf.int64, tf.int64))
    encoded_text.set_shape([None])
    label.set_shape([])
    return encoded_text, label


vocabulary_set = tok.tfds_tokens()
encoder = tfds.features.text.TokenTextEncoder(
    vocabulary_set, lowercase=False, strip_vocab=True)
encoder.save_to_file(OUTPUT_ENCODER_PATH)
encoded_dataset = dataset.map(encode_map)

for sentence, _ in dataset.take(1):
    print(sentence.numpy())

for encoded_sentence, _ in encoded_dataset.take(1):
    print(encoded_sentence.numpy())
    decode_sample_text = encoder.decode(encoded_sentence.numpy())
    print(decode_sample_text)
