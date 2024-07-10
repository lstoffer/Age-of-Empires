from typing import Optional
from utils.AgeType import AgeType
from Age import Age
from utils.Ressources import Ressources


class Ages:
    def __init__(self, agesDict: dict) -> None:
        self.ages = {
            AgeType(key): Age.from_dict(value) for key, value in agesDict.items()
        }

    def nextAge(self, age: AgeType) -> Optional[AgeType]:
        return self.ages[age].nextAge
    
    def nextAgeCost(self, age: AgeType) -> Ressources:
        return self.ages[age].costs

    def serialize(self):
        ages = {
            key.value: value.serialize() for key, value in self.ages.items()
        }
        return ages
