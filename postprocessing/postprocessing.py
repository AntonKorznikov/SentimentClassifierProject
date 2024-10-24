# postprocessing.py

import os
import json

OUTPUT_RAW_DIR = 'examples/output_raw'
OUTPUT_DIR = 'examples/output'

def postprocess():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    for filename in os.listdir(OUTPUT_RAW_DIR):
        if filename.endswith('.json'):
            with open(os.path.join(OUTPUT_RAW_DIR, filename), 'r') as f:
                data = json.load(f)
            with open(os.path.join(OUTPUT_DIR, filename.replace('.json', '.txt')), 'w') as f:
                f.write(f"Sentiment: {data['label']}, Score: {data['score']}\n")
    print("Postprocessing completed.")

if __name__ == "__main__":
    postprocess()
    