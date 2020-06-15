import os
import sys
from gensim.scripts.word2vec2tensor import word2vec2tensor


def main():
    file_name = input("Enter filename (without extension, bin file): ")
    path = os.path.abspath(
        __file__ + f"/../../../output/word_embedding")
    try:
        word2vec2tensor(f'{path}/{file_name}.kv', file_name, binary=True)
    except FileNotFoundError:
        print(
            f"File: '{path}/{file_name}.kv' no found. Maybe you forgot to format the '.model' file into a '.kv' file first?")
        print("Use the 'model_converter.py' first!")
        return
    print('Done! File is stored where this script was runnging form.')


if __name__ == "__main__":
    main()
