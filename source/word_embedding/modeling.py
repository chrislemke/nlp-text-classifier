import os
from gensim.scripts.word2vec2tensor import word2vec2tensor
from gensim.models import Word2Vec
from gensim import models
from paths import MODEL_PATH
from paths import INPUT_PATH
import sys
import nltk
import multiprocessing
import io
from gensim.models import FastText

nltk.download('punkt')


def converter():
    file_name = input(
        'Enter file which should be converted (without extension): ')
    binary = input('Binary? y/N ')
    model = Word2Vec.load(f'{MODEL_PATH}/{file_name}.model')
    if binary == "y":
        model.wv.save_word2vec_format(
            f'{MODEL_PATH}/{file_name}-bin.kv', binary=True)
    elif binary == "N":
        model.wv.save_word2vec_format(
            f'{MODEL_PATH}/{file_name}-txt.kv', binary=False)
    else:
        print("No valid choice was made!")


def w2v_continue_training():
    new_text_file = input(
        'New source file path (e.g text_to_model.txt): ')
    model_file = input(
        'Source file which should be trained (word2vec model): ')
    iterations = input('Iterations: ')

    with open(f'{INPUT_PATH}/{new_text_file}', encoding='UTF-8') as file:
        text = file.read()
        sentences = nltk.sent_tokenize(text, language='german')
        tokenized_text = []
        for sentence in sentences:
            if ' ' in sentence == False:
                continue
            if len(sentence) <= 20:
                continue
            tokenized_text.append(nltk.word_tokenize(
                sentence, language='german'))
    file.close()
    print(f'Created {len(tokenized_text)} tokens.')
    print('Short preview:')
    print(tokenized_text[:1])

    model = Word2Vec.load(f'{MODEL_PATH}/{model_file}')
    model.train(tokenized_text, total_examples=len(
        tokenized_text), epochs=int(iterations))
    file_name = model_file.replace('.model', '')
    file_name = f"{file_name}-RT"
    model.save(f'{MODEL_PATH}/{file_name}-W2V.model')
    print('\nDone!')
    also_converter = input('Do you also want to create an KV version? y/N ')
    if also_converter == "y":
        binary = input("Binary? y/N - 'XXL' for txt and binary: ")
        model = Word2Vec.load(f'{MODEL_PATH}/{file_name}.model')
        if binary == "y":
            model.wv.save_word2vec_format(
                f'{MODEL_PATH}/{file_name}-bin-W2V.kv', binary=True)
        elif binary == "N":
            model.wv.save_word2vec_format(
                f'{MODEL_PATH}/{file_name}-txt-W2V.kv', binary=False)
        elif binary == "XXL":
            model.wv.save_word2vec_format(
                f'{MODEL_PATH}/{file_name}-bin-W2V.kv', binary=True)
            model.wv.save_word2vec_format(
                f'{MODEL_PATH}/{file_name}-txt-W2V.kv', binary=False)
        else:
            print("No valid choice was made!")
    else:
        print("Bye!")


def word2vec_model():
    text_file = input('Source file path (e.g text_to_model.txt): ')
    model_prefix = input('Model prefix (e.g. phil, wiki, full): ')
    iterations = input('Iterations: ')
    size = input('Size: ')
    window = input('Window: ')
    min_count = input('Min count: ')
    identifier = input('ID (number): ')

    with open(f'{INPUT_PATH}/{text_file}', encoding='UTF-8') as file:
        text = file.read()
        sentences = nltk.sent_tokenize(text, language='german')
        tokenized_text = []
        for sentence in sentences:
            if ' ' in sentence == False:
                continue
            if len(sentence) <= 20:
                continue
            tokenized_text.append(nltk.word_tokenize(
                sentence, language='german'))
    print(f'Created {len(tokenized_text)} tokens.')
    file_name = f'{model_prefix}_{size}_iter{iterations}_win{window}_{identifier}'
    print('Short preview:')
    print(tokenized_text[:1])
    model = Word2Vec(tokenized_text, size=int(size), window=int(window), min_count=int(min_count),
                     negative=15, iter=int(iterations), workers=multiprocessing.cpu_count())
    model.save(f'{MODEL_PATH}/{file_name}-W2V.model')
    print('\nDone!')
    also_converter = input('Do you also want to create an KV version? y/N ')
    if also_converter == "y":
        binary = input("Binary? y/N - 'XXL' for txt and binary: ")
        model = Word2Vec.load(f'{MODEL_PATH}/{file_name}.model')
        if binary == "y":
            model.wv.save_word2vec_format(
                f'{MODEL_PATH}/{file_name}-bin-W2V.kv', binary=True)
        elif binary == "N":
            model.wv.save_word2vec_format(
                f'{MODEL_PATH}/{file_name}-txt-W2V.kv', binary=False)
        elif binary == "XXL":
            model.wv.save_word2vec_format(
                f'{MODEL_PATH}/{file_name}-bin-W2V.kv', binary=True)
            model.wv.save_word2vec_format(
                f'{MODEL_PATH}/{file_name}-txt-W2V.kv', binary=False)
        else:
            print("No valid choice was made!")
    else:
        print("Bye!")


def fast_text_model():
    text_file = input('Source file path (e.g text_to_model.txt): ')
    model_prefix = input('Model prefix (e.g. dta, wiki, dta_wiki, etc. ): ')
    iterations = input('Iterations: ')
    size = input('Size: ')
    window = input('Window: ')
    min_count = input('Min count: ')
    identifier = input('ID (number): ')

    with open(f'{INPUT_PATH}/{text_file}', encoding='UTF-8') as file:
        text = file.read()
        sentences = nltk.sent_tokenize(text, language='german')
        tokenized_text = []
        for sentence in sentences:
            if ' ' in sentence == False:
                continue
            if len(sentence) <= 20:
                continue
            tokenized_text.append(nltk.word_tokenize(
                sentence, language='german'))
    print(f'Created {len(tokenized_text)} tokens.')
    file_name = f'{model_prefix}_{size}_iter{iterations}_win{window}_{identifier}'
    print('Short preview:')
    print(tokenized_text[:1])

    model = FastText(size=int(size), window=int(
        window), min_count=int(min_count))
    model.build_vocab(sentences=tokenized_text)
    model.train(sentences=tokenized_text,
                total_examples=len(tokenized_text), epochs=int(iterations))
    model.save(f'{MODEL_PATH}/{file_name}-FT.model')


if __name__ == '__main__':
    globals()[sys.argv[1]]()
