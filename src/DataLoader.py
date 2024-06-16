import utils.Buildings as Buildings
import utils.Nations as Nations
from typing import Dict
import json
import os

cwd = os.getcwd()
building_data_filepath = os.path.join(cwd, 'data/buildings_data.json')

def load_data(filepath) -> Dict:
    try:
        with open(filepath, 'r') as file:
            try:
                data = json.load(file)
                return data
            except json.JSONDecodeError as e:
                print(f'Error decoding JSON file {filepath}: {e}')
    except FileNotFoundError:
        print(f'File {filepath} not found')
        return {}
    except PermissionError:
        print(f'Permission denied when trying to read {filepath}')
        return {}
    except Exception as e:
        print(f'Error loading file {filepath}: {e}')
        return {}


def load_building_data(building_type: Buildings = None, nation: Nations = None) -> Dict:
    data = load_data(building_data_filepath)
        
    if building_type is not None:
        try:
            data = data[building_type.value]
        except:
            print(f'Building type {building_type.value} not present in building data')
            return {}
    
    if nation is not None:
        try:
            data = data[nation.value]
        except:
            print(f'Nations {nation.value} not presetn in building data of building type {building_type.value}')
            return {}
    
    return data
            