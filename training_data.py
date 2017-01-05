import json
import warnings
from glob import glob
from itertools import groupby

class TrainingData(object):
    def __init__(self, data_path):
        self.skills = []

        self.min_examples_per_intent = 2

        self.load_data(data_path)
        self.validate()

    def as_json(self, **kwargs):
        return json.dumps({
            "skills": self.skills
        }, **kwargs)

    def load_data(self, path):
        data = {}
        for f in glob(path+'/*.json'):
            with open(f, encoding='utf-8') as skill_file:
                if(len(data) == 0):
                    data = json.loads(skill_file.read())
                else:
                    data["skills"] = data["skills"] + json.loads(skill_file.read())["skills"]
        skills = data.get("skills", list())

        self.skills = skills

    def validate(self):
        examples = sorted(self.skills, key=lambda e: e["intent"])
        skill = []
        for intent, group in groupby(examples, lambda e: e["intent"]):
            size = len(list(group))
            if size < self.min_examples_per_intent:
                template = "intent {0} has only {1} training examples! minimum is {2}, training may fail."
                warnings.warn(template.format(intent, size, self.min_examples_per_intent))
