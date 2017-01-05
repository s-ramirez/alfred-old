from classifier import SpacySklearnClassifier
from training_data import TrainingData

trainer = SpacySklearnClassifier()
data = TrainingData('skills/small_talk.json')

trainer.train(data)
print(trainer.parse("hola!"));
print(trainer.parse("goodbye"));
