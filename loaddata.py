"""
This module will read the movies data into Python
"""

# imports
import os
import json

# constants
CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
DATA_DIR = os.path.abspath(os.path.join(CURRENT_DIR, 'data'))
MOJO_DIR = os.path.join(DATA_DIR, 'boxofficemojo')

def load_mojo_data():
    movies=[]
    for file in os.listdir(MOJO_DIR):
        target_file_path = os.path.join(MOJO_DIR, file)
        with open(target_file_path, 'r') as target_file:
            movies.append(json.load(target_file))
    return movies
