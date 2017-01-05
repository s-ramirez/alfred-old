from actions.handler import ActionHandler

from analyzer.classifier import SpacySklearnClassifier
from analyzer.training_data import TrainingData

trainer = SpacySklearnClassifier()
data = TrainingData('skills')

trainer.train(data)
# print(trainer.parse("I'm looking for a place in the north of town"));
command = trainer.parse("Is it raining should I wear a sweater?")

actions = ActionHandler.get_actions()
response = actions[command["intent"]].respond({},command)
print(response)
