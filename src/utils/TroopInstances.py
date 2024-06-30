from utils.TroopType import TroopType
from Troop import Troop


class TroopInstances:
    def __init__(self, archer, infantry, cavalry, siege) -> None:
        self.archer = archer
        self.infantry = infantry
        self.cavalry = cavalry
        self.siege = siege

    @classmethod
    def from_dict(cls, dict):
        archer = Troop.from_dict(dict[TroopType.ARCHER])
        infantry = Troop.from_dict(dict[TroopType.INFANTRY])
        cavalry = Troop.from_dict(dict[TroopType.CAVALRY])
        siege = Troop.from_dict(dict[TroopType.SIEGE])
        return cls(archer, infantry, cavalry, siege)