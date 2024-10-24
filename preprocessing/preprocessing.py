# preprocessing.py

import os
import shutil

INPUT_RAW_DIR = 'examples/input_raw'
INPUT_DIR = 'examples/input'

def preprocess():
    if not os.path.exists(INPUT_DIR):
        os.makedirs(INPUT_DIR)
    for filename in os.listdir(INPUT_RAW_DIR):
        if filename.endswith('.txt'):
            shutil.copy(os.path.join(INPUT_RAW_DIR, filename), INPUT_DIR)
    print("Preprocessing completed.")

if __name__ == "__main__":
    preprocess()