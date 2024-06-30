from typing import List
from utils.UpdateType import UpdateType
from utils.AgeType import AgeType
from utils.Ressources import Ressources
from utils.Troops import Troops
from utils.Buildings import Buildings
from utils.BuildingInstances import BuildingInstances
from utils.TroopInstances import TroopInstances
from Villager import Villager

class Nation:
    def __init__(
        self,
        points: int,
        updates: List[UpdateType],
        age: AgeType,
        fields: List[int],
        ressources: Ressources,
        troops: Troops,
        buildings: Buildings,
        villagers: int,
        buildingInstances: BuildingInstances,
        troopInstances: TroopInstances,
        villagerInstance: Villager
    ) -> None:
        self.points = points
        self.updates = updates
        self.age = age
        self.fields = fields
        self.ressources = ressources
        self.troops = troops
        self.buildings = buildings
        self.villagers = villagers
        self.buildingInstances = buildingInstances
        self.toopInstances = troopInstances
        self.villagerInstance = villagerInstance

    @classmethod
    def from_dict(cls, nationDict: dict, buildingsDict: dict, troopsDict: dict, villagerDict: dict):
        points = nationDict['points']
        updates = [UpdateType(update) for update in nationDict['updates']]
        age = AgeType(nationDict['age'])
        fields = nationDict['fields']
        ressources = Ressources.from_dict(nationDict['ressources'])
        troops = Troops.from_dict(nationDict['troops'])
        buildings = Buildings.from_dict(nationDict['buildings'])
        villagers = nationDict['villagers']

        buildingInstances = BuildingInstances.from_dict(buildingsDict)
        troopIntances = TroopInstances.from_dict(troopsDict)
        villagerInstance = Villager.from_dict(villagerDict)

        return cls(points, updates, age, fields, ressources, troops, buildings, villagers, buildingInstances, troopIntances, villagerInstance)
