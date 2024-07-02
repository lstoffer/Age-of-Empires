from utils.RessourceType import RessourceType
from utils.NationType import NationType
from utils.Troops import Troops
from utils.Buildings import Buildings


class Field:
    '''
    Class that represents one field on the board
    '''
    def __init__(self, index: int, ressource: RessourceType, nation: NationType,
                 troops: Troops, buildings: Buildings, villagers: int) -> None:
        self.index = index
        self.ressource = ressource
        self.nation = nation
        self.troops = troops
        self.buildings = buildings
        self.villagers = villagers

    @classmethod
    def from_dict(cls, dict):
        index = dict['index']
        ressource = RessourceType(dict['ressource'])
        nation = NationType(dict['nation'])
        troops = Troops.from_dict(dict['troops'])
        buildings = Buildings.from_dict(dict['buildings'])
        villagers = dict['villagers']
        return cls(index, ressource, nation, troops, buildings, villagers)

    def getTroops(self) -> Troops:
        return self.troops

    def getVillager(self) -> int:
        return self.villagers

    def getNation(self) -> NationType:
        return self.nation

    def getRessource(self) -> RessourceType:
        return self.ressource

    def serialize(self) -> dict:
        fieldData = {}
        fieldData['index'] = self.index
        fieldData['ressource'] = self.ressource
        fieldData['nation'] = self.nation
        fieldData['troops'] = self.troops.serialize()
        fieldData['buildings'] = self.buildings.serialize()
        fieldData['villagers'] = self.villagers
        return fieldData
