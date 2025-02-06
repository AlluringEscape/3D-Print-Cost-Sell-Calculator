import json
import os

DATA_DIR = "data"
PRINTERS_FILE = os.path.join(DATA_DIR, "printers.json")
MATERIALS_FILE = os.path.join(DATA_DIR, "materials.json")
SETTINGS_FILE = os.path.join(DATA_DIR, "settings.json")

DEFAULT_SETTINGS = {
    "energy_cost": 0.15,
    "labor_cost": 20.00,
    "fail_rate": 10,
    "markup": 30
}

def load_settings():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR, exist_ok=True)
    try:
        with open(SETTINGS_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return DEFAULT_SETTINGS

def load_data(file):
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR, exist_ok=True)
    try:
        with open(file, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_data(data, file):
    with open(file, "w") as f:
        json.dump(data, f, indent=2)