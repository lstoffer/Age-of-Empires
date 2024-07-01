from utils.TroopType import TroopType

class Troops:
    def __init__(self, archer: int, infantry: int, cavalry: int, siege: int) -> None:
        self.archer = archer
        self.infantry = infantry
        self.cavalry = cavalry
        self.siege = siege

    @classmethod
    def from_dict(cls, dict):
        archer = dict[TroopType.ARCHER]
        infantry = dict[TroopType.INFANTRY]
        cavalry = dict[TroopType.CAVALRY]
        siege = dict[TroopType.SIEGE]
        return cls(archer, infantry, cavalry, siege)
    
    def serialize(self) -> dict:
        troopData = {}
        troopData[TroopType.ARCHER.value] = self.archer
        troopData[TroopType.INFANTRY.value] = self.infantry
        troopData[TroopType.CAVALRY.value] = self.cavalry
        troopData[TroopType.SIEGE.value] = self.siege
        return troopData
