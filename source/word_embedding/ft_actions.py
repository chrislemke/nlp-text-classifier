from gensim.models import FastText
import os
import sys
from values import FIRST_SENTENCE
from values import SECOND_SENTENCE
from paths import MODEL_PATH

FILE_NAME = "some_pg_300_iter30_win30_13-FT.model"


model = FastText.load(f"{MODEL_PATH}/ft/{FILE_NAME}")
word_vectors = model.wv


def diff_vector():
    positive_word = input("Positiv word: ")
    operator = input("Operator (+/-): ")
    negative_word = input("Negative word: ")

    if operator == '-':
        diff_vector = word_vectors[f'{positive_word}'] - \
            word_vectors[f'{negative_word}']
    elif operator == '+':
        diff_vector = word_vectors[f'{positive_word}'] - \
            word_vectors[f'{negative_word}']
    else:
        print("Invalid operator!")

    result = word_vectors.most_similar(positive=[diff_vector], topn=3)[2]
    print(result[0])



def similar():
    word = input("Enter the word: ")
    try:
        result = word_vectors.similar_by_word(word)
    except KeyError:
        print("Unknown vocabulary!")
        return
    print(result[:5])
    print('\n')


def negative():
    print("X - Y + Z (men - king + woman)")
    string = input("Input (without operators): ")
    list = string.split(' ')
    print('\n')

    try:
        result = word_vectors.most_similar(
            positive=[list[0], list[2]], negative=[list[1]])

    except KeyError:
        print("Unknown vocabulary!")
        return
    print(f'{list[0]} - {list[1]} + {list[2]} = {result[0]}')
    print('\n')


def sentence_distance():
    similarity = word_vectors.wmdistance(FIRST_SENTENCE, SECOND_SENTENCE)
    print('== sentence_distance ==')
    print(similarity)
    print('\n')


def not_match():
    words = input("Enter some words: ")
    try:
        print(f'--> {word_vectors.doesnt_match(words.split())}')
    except KeyError:
        print("Unknown vocabulary!")
        return


if __name__ == '__main__':
    globals()[sys.argv[1]]()
