# processing.py

import os
import json
from transformers import pipeline

INPUT_DIR = 'examples/input'
OUTPUT_RAW_DIR = 'examples/output_raw'

def process():
    if not os.path.exists(OUTPUT_RAW_DIR):
        os.makedirs(OUTPUT_RAW_DIR)
    classifier = pipeline('sentiment-analysis')
    for filename in os.listdir(INPUT_DIR):
        if filename.endswith('.txt'):
            with open(os.path.join(INPUT_DIR, filename), 'r') as f:
                text = f.read()
            result = classifier(text)[0]
            with open(os.path.join(OUTPUT_RAW_DIR, f"{filename[:-4]}.json"), 'w') as f:
                json.dump(result, f)
    print("Processing completed.")

if __name__ == "__main__":
    process()
