import json
import os

FILE_PATH = os.path.join(os.path.dirname(__file__), 'classes_data.json')

def load_classes():
    with open(FILE_PATH, 'r') as f:
        return json.load(f)

def save_classes(data):
    with open(FILE_PATH, 'w') as f:
        json.dump(data, f, indent=4)