from pathlib import Path
import json

__version__ = '2.0.1'
PROJECT_DIR = Path.cwd()
HERE = Path(__file__).parent

try:
    with open(f'{PROJECT_DIR}/package.json', 'r') as file:
        CONFIG = json.load(file)
except FileNotFoundError:
    CONFIG = None
