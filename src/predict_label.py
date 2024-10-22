from sentence_transformers import SentenceTransformer
from catboost import CatBoostClassifier


# change paths to config location
class Classifier:
    def __init__(
        self,
        encoder_path: str = "all-distilroberta-v1",
        classifier_path: str = "catboost_model.cbm",
    ) -> None:
        self.encoder = SentenceTransformer(encoder_path)
        self.classifier = CatBoostClassifier()
        self.classifier.load_model(classifier_path)

    def encode_and_classify(self, texts: str) -> int:
        encoded_seqs = self.encoder.encode(texts)
        return list(self.classifier.predict(encoded_seqs))[0]
