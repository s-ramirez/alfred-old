import json

from analyzer.classifier import SpacySklearnClassifier
from analyzer.training_data import TrainingData

from adapters.telegram import TelegramAdapter

settings = {}
with open('config.json', encoding="utf-8") as settings_file:
    settings = json.loads(settings_file.read())

classifier = SpacySklearnClassifier(settings)
data = TrainingData('skills')
classifier.train(data)

telegram = TelegramAdapter(settings["api_keys"]["telegram"], classifier)
print("Starting Telegram Adapter")
telegram.start_listening()
