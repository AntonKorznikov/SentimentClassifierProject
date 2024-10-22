import pandas as pd
import datasets
import pickle


from sklearn.metrics import f1_score
from sentence_transformers import SentenceTransformer
from sklearn.model_selection import train_test_split
from catboost import CatBoostClassifier
import torch
import numpy as np

df = pd.read_csv(
    "/Users/eneminova/SentimentClassifierProject/train_classifier/hatespeech_binary_dataset.csv",
    delimiter="\t",
)
# train_df = df[df.split == "train"]
# test_df = df[df.split == "test"]
# print(df[["sentiment", "text"]])

encoder = SentenceTransformer("all-distilroberta-v1")

# Assume `texts` is your text data, and `hate_scores` is the hate score feature
texts = list(df.text)
text_embeddings = encoder.encode(texts, batch_size=16, show_progress_bar=True)

with open("doc_embedding.pickle", "wb") as pkl:
    pickle.dump(text_embeddings, pkl)
# Combine embeddings with hate_score feature
# with open("doc_embedding.pickle", "rb") as pkl:
#     text_embeddings = pickle.load(pkl)


X = text_embeddings

# Define your labels (target variable)
y = df.labels  # Make sure labels are encoded as integers for CatBoost

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train CatBoost model
model = CatBoostClassifier(iterations=1000)
model.fit(X_train, y_train, verbose=100)
model.save_model("catboost_model.cbm")
test_texts = ["You are fucking whore!", "I love you", "I hate you"]
y_pred = model.predict(encoder.encode(test_texts))
# print(f1_score(y_test, y_pred, average="micro"))
print(y_pred)
