from utils.UpdateType import UpdateCategory
from utils.BuildingInstances import BuildingInstances
from utils.TroopInstances import TroopInstances
from Villager import Villager

class Update:
    '''
    Class that represents one Update with all its values
    The class contains instances for buildings, troops and villagers
    The instances hold the upate values for these categories of entities
    '''
    def __init__(self, buildingInstances: BuildingInstances, troopInstances: TroopInstances, villagerInstance: Villager) -> None:
        self.buildingInstances = buildingInstances
        self.troopInstances = troopInstances
        self.villagerInstance = villagerInstance

    @classmethod
    def from_dict(cls, dict):
        buildingInstances = BuildingInstances.from_dict(dict[UpdateCategory.BUILDINGS.value])
        troopInstances = TroopInstances.from_dict(dict[UpdateCategory.TROOPS.value])
        villager = Villager.from_dict(dict[UpdateCategory.VILLAGERS.value])
        return cls(buildingInstances, troopInstances, villager)

    def __add__(self, other):
        if isinstance(other, Update):
            return Update(self.buildingInstances + other.buildingInstances, 
                          self.troopInstances + other.troopInstances, 
                          self.villagerInstance + other.villagerInstance)
        return NotImplemented
