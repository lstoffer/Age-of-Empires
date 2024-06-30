import json
from pathlib import Path
from utils.NationType import NationType
from utils.TroopType import TroopType
from utils.BuildingType import BuildingType
from utils.UpdateType import UpdateType
from utils.UpdateType import UpdateCategory


class DataLoader():

    def __init__(self) -> None:
        self.dataDir = Path.cwd() / 'data'
        self.nationsData = self.loadData('nations_data.json')
        self.fieldsData = self.loadData('fields_data.json')
        self.villagersData = self.loadData('villagers_data.json')
        self.troopsData = self.loadData('troops_data.json')
        self.buildingsData = self.loadData('buildings_data.json')
        self.bordersData = self.loadData('borders_data.json')
        self.updatesData = self.loadData('updates_data.json')

    def loadData(self, fileName) -> dict:
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

    def nations(self, nationType: NationType = None) -> dict:
        if nationType:
            return self.nationsData[nationType].copy()
        else:
            return self.nationsData.copy()

    def fields(self, index: int = None) -> dict:
        if index:
            return self.fieldsData[str(index)].copy()
        else:
            return self.fieldsData.copy()

    def villagers(self, nationType: NationType = None) -> dict:
        if nationType:
            return self.villagersData[nationType].copy()
        else:
            return self.villagersData.copy()

    def troops(self, nationType: NationType = None, troopType: TroopType = None) -> dict:
        if nationType and troopType:
            return self.troopsData[nationType][troopType].copy()
        elif nationType:
            return self.troopsData[nationType].copy()
        else:
            return self.troopsData.copy()

    def buildings(self, nationType: NationType = None, buildingType: BuildingType = None) -> dict:
        if nationType and buildingType:
            return self.buildingsData[nationType][buildingType].copy()
        elif nationType:
            return self.buildingsData[nationType].copy()
        else:
            return self.buildingsData.copy()

    def updates(self, updateType: UpdateType = None, updateCategory: UpdateCategory = None, nationType: NationType = None) -> dict:
        if updateType and updateCategory and nationType:
            return self.updatesData[updateType][updateCategory][nationType].copy()
        elif updateType and updateCategory:
            return self.updatesData[updateType][updateCategory].copy()
        elif updateType:
            return self.updatesData[updateType].copy()
        else:
            return self.updatesData.copy()
    
    def borders(self) -> dict:
        return self.bordersData.copy()

