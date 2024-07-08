from utils.BuildingType import BuildingType

class Buildings:
    '''
    Class that represents the mumbers of diffrent building types that a nation
    posesses.    
    '''
    def __init__(self, towncenter, market, barracks, wall, castle, university) -> None:
        self.towncenter = towncenter
        self.market = market
        self.barracks = barracks
        self.wall = wall
        self.castle = castle
        self.university = university

    @classmethod
    def from_dict(cls, dict):
        towncenter = dict[BuildingType.TOWNCENTER.value]
        market = dict[BuildingType.MARKET.value]
        barracks = dict[BuildingType.BARRACKS.value]
        wall = dict[BuildingType.WALL.value]
        castle = dict[BuildingType.CASTLE.value]
        university = dict[BuildingType.UNIVERSITY.value]
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
