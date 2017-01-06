import json
from actions.handler import ActionHandler

from analyzer.classifier import SpacySklearnClassifier
from analyzer.training_data import TrainingData

trainer = SpacySklearnClassifier()
settings = {}

with open('config.json', encoding="utf-8") as settings_file:
    settings = json.loads(settings_file.read())

data = TrainingData('skills')

trainer.train(data)
# print(trainer.parse("I'm looking for a place in the north of town"));
# command = trainer.parse("Is it raining should I wear a sweater?")
command = trainer.parse("How's the weather in Paris?")

actions = ActionHandler.get_actions()
response = actions[command["intent"]].respond(settings,command)
print(response)
