import codecs
import json
import re
import warnings
from itertools import groupby

class TrainingData(object):
    def __init__(self, data_file):
        self.skills = []

        self.min_examples_per_intent = 2

        self.load_data(data_file)

    def as_json(self, **kwargs):
        return json.dumps({
            "skills": self.skills
        }, **kwargs)

    def load_data(self, filename):
        data = json.loads(open(filename, encoding='utf-8').read())
        skills = data.get("skills", list())

        self.skills = skills

    # def validate(self):
    #     examples = sorted(self.skills, key=lambda e: e["intent"])
    #     skill = []
    #     for intent, group in groupby(examples, lambda e: e["intent"]):
    #         size = len(list(group))
    #         if size < self.min_examples_per_intent:
    #             template = "intent {0} has only {1} training examples! minimum is {2}, training may fail."
    #             warnings.warn(template.format(intent, size, self.min_examples_per_intent))
