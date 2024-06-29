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
