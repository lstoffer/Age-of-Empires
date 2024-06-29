from utils.RessourceType import RessourceType
from utils.NationType import NationType
from utils.Troops import Troops
from utils.Buildings import Buildings
from utils.Ressources import Ressources

class Field:
    def __init__(self, index: int, ressource: RessourceType, nation: NationType, troops: Troops, buildings: Buildings, villagers: int) -> None:
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

    def getAttack(sef):
        pass

    def getDefence(self):
        pass
