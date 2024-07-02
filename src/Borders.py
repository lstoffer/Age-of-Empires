from typing import Optional
from utils.NationType import NationType


class Borders:
    def __init__(self, borders: dict) -> None:
        self.borders = {
            int(outerKey): {int(innerKey): (NationType(value) if value != "" else None) for innerKey, value in outerValue.items()}
            for outerKey, outerValue in borders.items()
        }

    def getBorder(self, fieldOne: int, fieldTwo: int) -> Optional[NationType]:
        return self.borders[fieldOne][fieldTwo]

    def addBorder(self, fieldOne: int, fieldTwo: int, nation: NationType):
        self.borders[fieldOne][fieldTwo] = nation
        self.borders[fieldTwo][fieldOne] = nation

    def removeBorder(self, fieldOne: int, fieldTwo: int):
        self.borders[fieldOne][fieldTwo] = None
        self.borders[fieldTwo][fieldOne] = None

    def serialize(self) -> dict:
        borders = {
            str(outerKey): {str(innerKey): (nation.value if nation is not None else "") for innerKey, nation in outerValue.items()}
            for outerKey, outerValue in self.borders.items()
        }
        return borders