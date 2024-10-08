from utils.UpdateType import UpdateCategory
from utils.BuildingInstances import BuildingInstances
from utils.TroopInstances import TroopInstances
from Villager import Villager
from utils.Ressources import Ressources

class Update:
    '''
    Class that represents one Update with all its values
    The class contains instances for buildings, troops and villagers
    The instances hold the upate values for these categories of entities
    '''
    def __init__(self, cost: Ressources, buildingInstances: BuildingInstances, troopInstances: TroopInstances, villagerInstance: Villager) -> None:
        self.cost = cost
        self.buildingInstances = buildingInstances
        self.troopInstances = troopInstances
        self.villagerInstance = villagerInstance

    @classmethod
    def from_dict(cls, dict):
        costs = Ressources.from_dict(dict[UpdateCategory.COSTS.value])
        buildingInstances = BuildingInstances.from_dict(dict[UpdateCategory.BUILDINGS.value])
        troopInstances = TroopInstances.from_dict(dict[UpdateCategory.TROOPS.value])
        villager = Villager.from_dict(dict[UpdateCategory.VILLAGERS.value])
        return cls(costs, buildingInstances, troopInstances, villager)

    def __add__(self, other):
        if isinstance(other, Update):
            return Update(self.cost,
                          self.buildingInstances + other.buildingInstances,
                          self.troopInstances + other.troopInstances, 
                          self.villagerInstance + other.villagerInstance)
        return NotImplemented
