from typing import Optional
from utils.NationType import NationType


class Borders:
    def __init__(self, borders: dict) -> None:
        self.borders = {
            int(outerKey): {int(innerKey): (NationType(value) if value != "" else NationType.NONE) for innerKey, value in outerValue.items()}
            for outerKey, outerValue in borders.items()
        }

    def isNeighbour(self, fieldOne: int, fieldTwo: int) -> bool:
        if fieldTwo in self.borders[fieldOne] and fieldOne in self.borders[fieldTwo]:
            return True
        else:
            return False

    def getBorder(self, fieldOne: int, fieldTwo: int) -> Optional[NationType]:
        return self.borders[fieldOne][fieldTwo]

    def addWall(self, nation: NationType, fieldOne: int, fieldTwo: int):
        if not self.isNeighbour(fieldOne, fieldTwo):
            raise Exception(f'Not able to add wall: {fieldOne} and {fieldTwo} are no neighbours')
        if self.borders[fieldTwo][fieldOne] != NationType.NONE:
            wallNation = self.borders[fieldOne][fieldTwo]
            raise Exception(
                f'Not able to add wall for {nation}, '
                f'{wallNation} already has a wall on border between {fieldOne} and {fieldTwo}'
            )
        self.borders[fieldOne][fieldTwo] = nation
        self.borders[fieldTwo][fieldOne] = nation

    def destroyWall(self, fieldOne: int, fieldTwo: int):
        if not self.isNeighbour(fieldOne, fieldTwo):
            raise Exception(f'Not able to destroy wall: {fieldOne} and {fieldTwo} are no neighbours')
        self.borders[fieldOne][fieldTwo] = NationType.NONE
        self.borders[fieldTwo][fieldOne] = NationType.NONE

    def serialize(self) -> dict:
        borders = {
            str(outerKey): {str(innerKey): (nation.value if nation is not NationType.NONE else "") for innerKey, nation in outerValue.items()}
            for outerKey, outerValue in self.borders.items()
        }
        return borders
