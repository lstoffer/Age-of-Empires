from utils.BuildingType import BuildingType
from Building import Building

class BuildingInstances:
    def __init__(self, towncenter: Building = None, market: Building = None, barracks: Building = None, wall: Building = None, castle: Building = None, university: Building = None) -> None:
        self.towncenter = towncenter
        self.market = market
        self.barracks = barracks
        self.wall = wall
        self.castle = castle
        self.university = university

    @classmethod
    def from_dict(cls, dict):
        towncenter = Building.from_dict(dict[BuildingType.TOWNCENTER])
        market = Building.from_dict(dict[BuildingType.MARKET])
        barracks = Building.from_dict(dict[BuildingType.BARRACKS])
        wall = Building.from_dict(dict[BuildingType.WALL])
        castle = Building.from_dict(dict[BuildingType.CASTLE])
        university = Building.from_dict(dict[BuildingType.UNIVERSITY])
        return cls(towncenter, market, barracks, wall, castle, university)