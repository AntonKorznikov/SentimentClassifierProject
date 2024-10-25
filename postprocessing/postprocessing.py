import os
import json

OUTPUT_RAW_DIR = "examples/output_raw"
OUTPUT_DIR = "examples/output"


def postprocess():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    for filename in os.listdir(OUTPUT_RAW_DIR):
        if filename.endswith(".json"):
            with open(os.path.join(OUTPUT_RAW_DIR, filename), "r") as f:
                results = json.load(f)

            # Formulate a summary output
            output_content = ""
            for result in results:
                output_content += (
                    f"Sentiment: {result['label']}, Score: {result['score']}\n"
                )

            with open(
                os.path.join(OUTPUT_DIR, filename.replace(".json", ".txt")), "w"
            ) as out_file:
                out_file.write(output_content)

    print("Postprocessing completed.")


if __name__ == "__main__":
    postprocess()
