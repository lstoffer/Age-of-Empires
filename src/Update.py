from utils.UpdateType import UpdateCategory
from utils.BuildingInstances import BuildingInstances
from utils.TroopInstances import TroopInstances
from Villager import Villager

class Update:
    def __init__(self, buildingInstances: BuildingInstances, troopInstances: TroopInstances, villager: Villager) -> None:
        self.buildingInstances = buildingInstances
        self.troopInstances = troopInstances
        self.villager = villager

    @classmethod
    def from_dict(cls, dict):
        buildingInstances = BuildingInstances.from_dict(dict[UpdateCategory.BUILDINGS])
        troopInstances = TroopInstances.from_dict(dict[UpdateCategory.TROOPS])
        villager = Villager.from_dict(dict[UpdateCategory.VILLAGERS])
        return cls(buildingInstances, troopInstances, villager)

    def __add__(self, other):
        if isinstance(other, Update):
            return Update(self.buildingInstances + other.buildingInstances, 
                          self.troopInstances + other.troopInstances, 
                          self.villager + other.villager)
        return NotImplemented
