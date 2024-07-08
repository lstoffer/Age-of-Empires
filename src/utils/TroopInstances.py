from utils.TroopType import TroopType
from Troop import Troop


class TroopInstances:
    '''
    Container Class for the troop instances of one nation
    '''
    def __init__(self, archer: Troop, infantry: Troop, cavalry: Troop, siege: Troop) -> None:
        self.archer = archer
        self.infantry = infantry
        self.cavalry = cavalry
        self.siege = siege

    @classmethod
    def from_dict(cls, dict):
        archer = Troop.from_dict(dict[TroopType.ARCHER.value])
        infantry = Troop.from_dict(dict[TroopType.INFANTRY.value])
        cavalry = Troop.from_dict(dict[TroopType.CAVALRY.value])
        siege = Troop.from_dict(dict[TroopType.SIEGE.value])
        return cls(archer, infantry, cavalry, siege)
    
    def __add__(self, other):
        if isinstance(other, TroopInstances):
            return TroopInstances(self.archer + other.archer,
                                  self.infantry + other.infantry,
                                  self.cavalry + other.cavalry,
                                  self.siege + other.siege)
        return NotImplemented