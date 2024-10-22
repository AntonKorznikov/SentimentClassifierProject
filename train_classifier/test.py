# from simpletransformers.classification import ClassificationModel, ClassificationArgs
# from sklearn.metrics import f1_score
# import pandas as pd
# import logging
# import datasets

# if __name__ == "__main__":

#     logging.basicConfig(level=logging.INFO)
#     transformers_logger = logging.getLogger("transformers")
#     transformers_logger.setLevel(logging.WARNING)

#     # Preparing train data
#     df = pd.read_csv("./hatespeech_binary_dataset.csv", delimiter="\t")
#     train_df = df[df.split == "train"]
#     eval_df = df[df.split == "test"]

#     # Preparing eval data

#     # Optional model configuration
#     model_args = ClassificationArgs(num_train_epochs=1)

#     # Create a ClassificationModel
#     model = ClassificationModel(
#         "bert", "bert-base-cased", num_labels=5, args=model_args, use_cuda=False
#     )

#     # Train the model
#     model.train_model(train_df)

#     # Evaluate the model
#     # result, model_outputs, wrong_predictions = model.eval_model(eval_df)

#     # Make predictions with the model
#     predictions, raw_outputs = model.predict(eval_df.text)

#     # print("Predictions:", predictions)
#     # print("Raw outputs:", raw_outputs)
#     print(f1_score(eval_df.text.labels, predictions, average="macro"))
import os
from dotenv import load_dotenv

load_dotenv()
print(os.environ["API_TOKEN"])
