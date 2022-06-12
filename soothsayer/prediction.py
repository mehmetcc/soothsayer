from dataclasses import dataclass
from flair.models import TextClassifier
from flair.data import Sentence, Label

from typing import Optional

"""
These might be terribly wrong. Honestly I am not well-versed in the field of cutting-edge NLP.
"""


@dataclass
class PredictionResult:
    text: str
    value: Optional[str]
    score: Optional[float]


class PredictionService:
    def __init__(self) -> None:
        self.classifier = TextClassifier.load('en-sentiment')

    def predict(self, text: str):
        result = self._predict(text)
        return PredictionResult(text, result.value, result.score)

    def _predict(self, text: str) -> Label:
        sentence = Sentence(text)
        self.classifier.predict(sentence)
        return sentence.labels[0]
