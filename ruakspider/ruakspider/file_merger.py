import os
import os.path
import shutil
import glob

ROOT_DIR = os.path.abspath(
    __file__ + f"/../../loaded/")
OUTPUT = os.path.abspath(
    __file__ + f"/../../output/__merged_file.txt")

open(OUTPUT, 'a').close()
with open(OUTPUT, 'w', encoding='UTF-8') as wf:
    for f in os.listdir(ROOT_DIR):
        if f == '.DS_Store':
            continue
        print(f)
        with open(f'{ROOT_DIR}/{f}', 'r', encoding='UTF-8') as rf:
            shutil.copyfileobj(rf, wf)
