import json
from pathlib import Path
from utils.NationType import NationType
from utils.TroopType import TroopType
from utils.BuildingType import BuildingType
from utils.UpdateType import UpdateType
from utils.UpdateType import UpdateCategory


class DataAccess():

    def __init__(self) -> None:
        self.dataDir = Path.cwd().parent / 'data'
        self.nationsData = self.loadData('nations_data.json')
        self.fieldsData = self.loadData('fields_data.json')
        self.villagersData = self.loadData('villagers_data.json')
        self.troopsData = self.loadData('troops_data.json')
        self.buildingsData = self.loadData('buildings_data.json')
        self.bordersData = self.loadData('borders_data.json')
        self.updatesData = self.loadData('updates_data.json')
        self.pointsData = self.loadData('points_data.json')
        self.agesData = self.loadData('age_data.json')

    def loadData(self, fileName: Path) -> dict:
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

    def storeData(self, fileName: Path, dataDict: dict):
        filePath = self.dataDir / fileName
        try:
            with open(filePath, 'w') as dataFile:
                json.dump(dataDict, dataFile)
        except Exception as e:
            print(f'Failed to overwirte {filePath}: {e}')

    def nations(self, nationType: NationType = None) -> dict:
        if nationType:
            return self.nationsData[nationType]
        else:
            return self.nationsData

    def fields(self, index: int = None) -> dict:
        if index:
            return self.fieldsData[str(index)]
        else:
            return self.fieldsData

    def villagers(self, nationType: NationType = None) -> dict:
        if nationType:
            return self.villagersData[nationType]
        else:
            return self.villagersData

    def troops(self, nationType: NationType = None, troopType: TroopType = None) -> dict:
        if nationType and troopType:
            return self.troopsData[nationType][troopType]
        elif nationType:
            return self.troopsData[nationType]
        else:
            return self.troopsData

    def buildings(self, nationType: NationType = None, buildingType: BuildingType = None) -> dict:
        if nationType and buildingType:
            return self.buildingsData[nationType][buildingType]
        elif nationType:
            return self.buildingsData[nationType]
        else:
            return self.buildingsData

    def updates(self, updateType: UpdateType = None, updateCategory: UpdateCategory = None,
                nationType: NationType = None) -> dict:
        if updateType and updateCategory and nationType:
            return self.updatesData[updateType][updateCategory][nationType]
        elif updateType and updateCategory:
            return self.updatesData[updateType][updateCategory]
        elif updateType:
            return self.updatesData[updateType]
        else:
            return self.updatesData

    def borders(self) -> dict:
        return self.bordersData

    def points(self) -> dict:
        return self.pointsData

    def ages(self) -> dict:
        return self.agesData
