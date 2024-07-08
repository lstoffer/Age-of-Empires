from utils.BuildingType import BuildingType
from Building import Building

class BuildingInstances:
    '''
    Container Class for the building instances of one nation
    '''
    def __init__(self, towncenter: Building = None, market: Building = None, barracks: Building = None, wall: Building = None, castle: Building = None, university: Building = None) -> None:
        self.towncenter = towncenter
        self.market = market
        self.barracks = barracks
        self.wall = wall
        self.castle = castle
        self.university = university

    @classmethod
    def from_dict(cls, dict):
        towncenter = Building.from_dict(dict[BuildingType.TOWNCENTER.value])
        market = Building.from_dict(dict[BuildingType.MARKET.value])
        barracks = Building.from_dict(dict[BuildingType.BARRACKS.value])
        wall = Building.from_dict(dict[BuildingType.WALL.value])
        castle = Building.from_dict(dict[BuildingType.CASTLE.value])
        university = Building.from_dict(dict[BuildingType.UNIVERSITY.value])
        return cls(towncenter, market, barracks, wall, castle, university)
    
    def __add__(self, other):
        if isinstance(other, BuildingInstances):
            return BuildingInstances(self.towncenter + other.towncenter,
                                     self.market + other.market,
                                     self.barracks + other.barracks,
                                     self.wall + other.wall,
                                     self.castle + other.castle,
                                     self.university + other.university)
        return NotImplemented