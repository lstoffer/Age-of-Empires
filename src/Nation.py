from typing import List
from utils.UpdateType import UpdateType
from utils.AgeType import AgeType
from utils.Ressources import Ressources
from utils.Troops import Troops
from utils.Buildings import Buildings


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
        villagers: int
    ) -> None:
        self.points = points
        self.updates = updates
        self.age = age
        self.fields = fields
        self.ressources = ressources
        self.troops = troops
        self.buildings = buildings
        self.villagers = villagers

    @classmethod
    def from_dict(cls, dict):
        points = dict['points']
        updates = [UpdateType(update) for update in dict['updates']]
        age = AgeType(dict['age'])
        fields = dict['fields']
        ressources = Ressources.from_dict(dict['ressources'])
        troops = Troops.from_dict(dict['troops'])
        buildings = Buildings.from_dict(dict['buildings'])
        villagers = dict['villagers']
        return cls(points, updates, age, fields, ressources, troops, buildings, villagers)
