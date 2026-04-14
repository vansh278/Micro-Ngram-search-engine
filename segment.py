import json
import os

class Segment:
    def __init__(self, path):
        self.path = path

    def write(self, index_data):
        with open(self.path, 'w') as f:
            json.dump({k: list(v) for k, v in index_data.items()}, f)

    def read(self):
        with open(self.path, 'r') as f:
            return json.load(f)
