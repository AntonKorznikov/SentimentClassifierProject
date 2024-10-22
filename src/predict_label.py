from sentence_transformers import SentenceTransformer
from catboost import CatBoostClassifier
import os


# change paths to config location
class Classifier:
    def __init__(
        self,
        encoder_path: str = "all-distilroberta-v1",
        classifier_path: str = "./src/catboost_model.cbm",
    ) -> None:
        self.encoder = SentenceTransformer(encoder_path)
        print(os.listdir("."))
        self.classifier = CatBoostClassifier()
        self.classifier.load_model(classifier_path)

    def encode_and_classify(self, texts: str) -> int:
        print("ENCODING STARTED")
        encoded_seqs = self.encoder.encode(texts)
        print("ENCODING ENDED")
        return list(self.classifier.predict(encoded_seqs))[0]
