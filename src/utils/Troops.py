from utils.TroopType import TroopType

class Troops:
    '''
    Class that represents the mumbers of diffrent troop types that a nation
    posesses.    
    '''
    def __init__(self, archer: int, infantry: int, cavalry: int, siege: int) -> None:
        self.archer = archer
        self.infantry = infantry
        self.cavalry = cavalry
        self.siege = siege

    @classmethod
    def from_dict(cls, dict):
        archer = dict[TroopType.ARCHER.value]
        infantry = dict[TroopType.INFANTRY.value]
        cavalry = dict[TroopType.CAVALRY.value]
        siege = dict[TroopType.SIEGE.value]
        return cls(archer, infantry, cavalry, siege)
    
    def serialize(self) -> dict:
        troopData = {}
        troopData[TroopType.ARCHER.value] = self.archer
        troopData[TroopType.INFANTRY.value] = self.infantry
        troopData[TroopType.CAVALRY.value] = self.cavalry
        troopData[TroopType.SIEGE.value] = self.siege
        return troopData
