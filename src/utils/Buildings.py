from utils.BuildingType import BuildingType

class Buildings:
    def __init__(self, towncenter, market, barracks, wall, castle, university) -> None:
        self.towncenter = towncenter
        self.market = market
        self.barracks = barracks
        self.wall = wall
        self.castle = castle
        self.university = university

    @classmethod
    def from_dict(cls, dict):
        towncenter = dict[BuildingType.TOWNCENTER]
        market = dict[BuildingType.MARKET]
        barracks = dict[BuildingType.BARRACKS]
        wall = dict[BuildingType.WALL]
        castle = dict[BuildingType.CASTLE]
        university = dict[BuildingType.UNIVERSITY]
        return cls(towncenter, market, barracks, wall, castle, university)
    
    def serialize(self) -> dict:
        buildingsData = {}
        buildingsData[BuildingType.TOWNCENTER.value] = self.towncenter
        buildingsData[BuildingType.MARKET.value] = self.market
        buildingsData[BuildingType.BARRACKS.value] = self.barracks
        buildingsData[BuildingType.WALL.value] = self.wall
        buildingsData[BuildingType.CASTLE.value] = self.castle
        buildingsData[BuildingType.UNIVERSITY.value] = self.university
        return buildingsData
