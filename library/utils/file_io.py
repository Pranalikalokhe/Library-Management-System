import json
import os

def load_data(file_path):
    if not os.path.exists(file_path):
        return []
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except json.JSONDecodeError:
        print(f"Error decoding {file_path}, loading empty list.")
        return []

def save_data(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
