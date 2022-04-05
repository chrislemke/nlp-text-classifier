import os
import os.path
import shutil
import glob
import sys

ROOT_DIR = os.path.abspath(__file__ + f"/../loaded")
OUTPUT = os.path.abspath(__file__ + f"/../output/_merged_file.txt")


def merge():
    for subdir, _, files in os.walk(ROOT_DIR):
        if subdir == ROOT_DIR:
            continue
        open(OUTPUT, "a").close()
        with open(OUTPUT, "w", encoding="UTF-8") as wf:
            for filename in files:
                if filename == ".DS_Store":
                    continue
                filepath = subdir + os.sep + filename
                with open(filepath, "r", encoding="UTF-8") as rf:
                    shutil.copyfileobj(rf, wf)
                print(f"Merged: {filename}")


merge()
