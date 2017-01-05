from analyzer.classifier import SpacySklearnClassifier
from analyzer.training_data import TrainingData

trainer = SpacySklearnClassifier()
data = TrainingData('skills')

trainer.train(data)
# print(trainer.parse("hola"));
# print(trainer.parse("goodbye"));
print(trainer.parse("Is it raining should I wear a sweater?"))
print(trainer.parse("I'm looking for a place in the north of town"));
