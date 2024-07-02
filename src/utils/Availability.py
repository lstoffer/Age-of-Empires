from utils.BuildingType import BuildingType
from utils.AgeType import AgeType
from utils.UpdateType import UpdateType

class Availability:
    def __init__(self, availability: dict) -> None:
        self.availability = {}
        self.availability['buildings'] = {
            BuildingType(outerKey): {AgeType(innerKey): value for innerKey, value in outerValue.items()}
            for outerKey, outerValue in availability['buildings'].items()
        }
        self.availability['updates'] = {
            UpdateType(outerKey): {AgeType(innerKey): value for innerKey, value in outerValue.items()}
            for outerKey, outerValue in availability['updates'].items()
        }

    def updateAvailable(self, update: UpdateType, age: AgeType) -> bool:
        return self.availability['upates'][update][age]
    
    def buildingAvailable(self, building: BuildingType, age: AgeType) -> bool:
        return self.availability['buildings'][building][age]
    
    def serialize(self):
        availability = {}
        availability['buildings'] = {
            outerKey.value: {innerKey.value: value for innerKey, value in outerValue.items()}
            for outerKey, outerValue in self.availability['buildings'].items()
        }
        availability['updates'] = {
            outerKey.value: {innerKey.value: value for innerKey, value in outerValue.items()}
            for outerKey, outerValue in self.availability['updates'].items()
        }