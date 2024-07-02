from typing import List
from utils.Ressources import Ressources
from utils.BuildingType import BuildingType
from utils.AgeType import AgeType


class Age:
    def __init__(self, costs: Ressources, buildingRequirements: List[BuildingType], nextAge: AgeType) -> None:
        self.costs = costs
        self.buildingRequirements = buildingRequirements
        self.nextAge = nextAge

    @classmethod
    def from_dict(cls, ageDict):
        costs = Ressources.from_dict(ageDict['costs'])
        buildingRequirements = [BuildingType(building) for building in ageDict['buildings']]
        nextAge = AgeType(ageDict['next']) if ageDict['next'] != "" else None
        return cls(costs, buildingRequirements, nextAge)

    def serialize(self):
        age = {}
        age['costs'] = self.costs.serialize()
        age['buildings'] = [building.value for building in self.buildingRequirements]
        age['next'] = self.nextAge.value
        return age
