import os
import json
from transformers import pipeline

INPUT_DIR = "examples/input"
OUTPUT_RAW_DIR = "examples/output_raw"


def process():
    if not os.path.exists(OUTPUT_RAW_DIR):
        os.makedirs(OUTPUT_RAW_DIR)

    classifier = pipeline(model="distilbert-base-uncased-finetuned-sst-2-english")

    all_results = []  # List to hold results for all sentences

    for filename in os.listdir(INPUT_DIR):
        if filename.endswith(".txt"):
            with open(os.path.join(INPUT_DIR, filename), "r") as f:
                sentences = f.readlines()

            # Process each sentence in the file
            for sentence in sentences:
                sentence = sentence.strip()  # Remove leading/trailing whitespace
                if sentence:
                    result = classifier(sentence)[0]
                    all_results.append(result)

            # Write all results to a single output file
            output_filename = f"{filename[:-4]}.json"
            with open(os.path.join(OUTPUT_RAW_DIR, output_filename), "w") as out_file:
                json.dump(all_results, out_file)

    print("Processing completed.")


if __name__ == "__main__":
    process()
