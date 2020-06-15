import os
import os.path
import shutil
import glob
import sys
from sourcespider.sourcespider import cleaner

ROOT_DIR = os.path.abspath(
    __file__ + f"/../input/source")
OUTPUT = os.path.abspath(
    __file__ + f"/../input/processed/_x_merged_file.txt")


def merge():
    for subdir, _, files in os.walk(ROOT_DIR):
        if subdir == ROOT_DIR:
            continue
        open(OUTPUT, 'a').close()
        with open(OUTPUT, 'w', encoding='UTF-8') as wf:
            for filename in files:
                if filename == '.DS_Store':
                    continue
                filepath = subdir + os.sep + filename
                with open(filepath, 'r', encoding='UTF-8') as rf:
                    shutil.copyfileobj(rf, wf)
                print(f"Merged: {filename}")


def dta_prepare_files():
    source_dir = input("Enter dir containing the files: ")

    cleaned_dir = f'{source_dir}/cleaned'
    try:
        os.mkdir(cleaned_dir)
    except:
        pass

    for filename in os.listdir(source_dir):
        if filename == 'cleaned':
            continue
        if filename == '.DS_Store':
            continue
        with open(f'{source_dir}/{filename}', 'r', encoding='UTF-8') as rf:
            text = rf.read()
            text = cleaner.dta_clean_up(text)
            with open(f'{cleaned_dir}/{filename}', 'w', encoding='UTF-8') as wf:
                wf.write(text)
                print(f"Created: {filename}")


if __name__ == '__main__':
    globals()[sys.argv[1]]()
