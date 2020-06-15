import os
import sys
from gensim.models import Word2Vec
import numpy as np
import tensorflow as tf

MODEL_PATH = os.path.abspath(
    __file__ + f"/../../../output/word2vec")


def embedding_matrix(model_name):
    model = Word2Vec.load(f'{MODEL_PATH}/{model_name}')
    embedding_matrix = np.zeros((len(model.wv.vocab), model.vector_size))
    for i in range(len(model.wv.vocab)):
        embedding_vector = model.wv[model.wv.index2word[i]]
        if embedding_vector is not None:
            embedding_matrix[i] = embedding_vector
    print(f"Embedding_matrix shape: {embedding_matrix.shape}")
    return embedding_matrix
