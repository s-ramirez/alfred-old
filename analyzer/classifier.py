import spacy
import os
import datetime
import json
import cloudpickle

from analyzer.feature_analyzer import Featurizer
from analyzer.intent_classifier import IntentClassifier
from analyzer.entity_extractor import EntityExtractor


class SpacySklearnClassifier():

    def __init__(self):
        self.training_data = None
        self.nlp = spacy.load('en', parser=False, entity=False)
        self.featurizer = Featurizer(self.nlp)
        self.intent_classifier = IntentClassifier()
        self.entity_extractor = EntityExtractor()

    def train(self, data):
        self.training_data = data
        self.train_entity_extractor(data.skills)
        self.train_intent_classifier(data.skills)

    def train_entity_extractor(self, entity_examples):
        self.entity_extractor.train(self.nlp, entity_examples)

    def train_intent_classifier(self, intent_examples):
        labels = [e["intent"] for e in intent_examples]
        sentences = [e["text"] for e in intent_examples]
        y = self.intent_classifier.transform_labels(labels)
        X = self.featurizer.create_bow_vecs(sentences)
        self.intent_classifier.train(X, y)

    def get_intent(self, text):
        X = self.featurizer.create_bow_vecs([text])
        return self.intent_classifier.predict(X)[0]

    def parse(self, text):
        preprocessesed = text.lower()
        intent = self.get_intent(preprocessesed)
        entities = self.entity_extractor.extract_entities(self.nlp, text)

        return {'text': text, 'intent': intent, 'entities': entities}
