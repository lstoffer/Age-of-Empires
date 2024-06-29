import json
from pathlib import Path


class DataLoader():

    def __init__(self) -> None:
        self.dataDir = Path.cwd() / 'data'
        self.nationsData = self.load_data('nations_data.json')
        self.fieldsData = self.load_data('fields_data.json')
        self.villagersData = self.load_data('villagers_data.json')
        self.troopsData = self.load_data('troops_data.json')
        self.buildingsData = self.load_data('buildings_data.json')
        self.bordersData = self.load_data('borders_data.json')
        self.updatesData = self.load_data('updates_data.json')

    def load_data(self, fileName) -> dict:
        filepath = self.dataDir / fileName
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

    def nations(self) -> dict:
        return self.nationsData.copy()

    def fields(self) -> dict:
        return self.fieldsData.copy()

    def villagers(self) -> dict:
        return self.villagersData.copy()

    def troops(self) -> dict:
        return self.troopsData.copy()

    def buildings(self) -> dict:
        return self.buildingsData.copy()

    def borders(self) -> dict:
        return self.bordersData.copy()

    def updates(self) -> dict:
        return self.updatesData.copy()
