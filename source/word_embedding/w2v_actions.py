from gensim.models import Word2Vec
import os
import sys
from values import FIRST_SENTENCE
from values import SECOND_SENTENCE
from paths import MODEL_PATH

# FILE_NAME = "wiki_de_dta_pg_philo_at_500_iter10_win30_10_W2V.model"
FILE_NAME = "full_700_iter100_win7_8.model"
# FILE_NAME = "full_700_iter100_win7_8-RT.model"


model = Word2Vec.load(f"{MODEL_PATH}/w2v/{FILE_NAME}")
word_vectors = model.wv


def diff_vector():
    positive_word = input("First word: ")
    operator = input("Operator (+/-): ")
    negative_word = input("Second word: ")

    if operator == '-':
        diff_vector = word_vectors[f'{positive_word}'] - \
            word_vectors[f'{negative_word}']
    elif operator == '+':
        diff_vector = word_vectors[f'{positive_word}'] + \
            word_vectors[f'{negative_word}']
    else:
        print("Invalid operator!")

    result = word_vectors.most_similar(positive=[diff_vector], topn=3)[2]
    print(result)


def similar():
    word = input("Enter the word: ")
    try:
        result = word_vectors.similar_by_word(word)
    except KeyError:
        print("Unknown vocabulary!")
        return
    print(result[:9])
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
    print(f'{list[0]} - {list[1]} + {list[2]} = {result[0]}, {result[1]}')
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
