import json
from pathlib import Path
from utils.DataType import DataType
from utils.NationType import NationType
from utils.TroopType import TroopType
from utils.BuildingType import BuildingType


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

    def nations(self) -> dict:
        return self.nationsData.copy()
    
    def nation(self, nationType: NationType) -> dict:
        return self.nationsData[nationType].copy()

    def fields(self) -> dict:
        return self.fieldsData.copy()
    
    def field(self, index: int) -> dict:
        return self.fieldsData[index].copy()

    def villagers(self, dataType: DataType = None, nationType: NationType = None) -> dict:
        if dataType and nationType:
            return self.villagersData[dataType][nationType].copy()
        elif dataType:
            return self.villagersData[dataType].copy()
        else:
            return self.villagersData.copy()

    def troops(self, dataType: DataType = None, nationType: NationType = None, troopType: TroopType = None) -> dict:
        if dataType and nationType and troopType:
            return self.troopsData[dataType][nationType][troopType].copy()
        elif dataType and nationType:
            return self.troopsData[dataType][nationType].copy()
        elif dataType:
            return self.troopsData[dataType].copy()
        else:
            return self.troopsData.copy()

    def buildings(self, dataType: DataType = None, buildingType: BuildingType = None) -> dict:
        if dataType and buildingType:
            return self.buildingsData[dataType][buildingType].copy()
        elif dataType:
            return self.buildingsData[dataType].copy()
        else:
            return self.buildingsData.copy()

    def borders(self) -> dict:
        return self.bordersData.copy()

    def updates(self) -> dict:
        return self.updatesData.copy()
