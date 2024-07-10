from utils.BuildingType import BuildingType

class Buildings:
    '''
    Class that represents the mumbers of diffrent building types that a nation
    posesses.    
    '''
    def __init__(self, towncenter: int, market: int, barracks: int, wall: int, castle: int, university: int) -> None:
        self.towncenter = towncenter
        self.market = market
        self.barracks = barracks
        self.wall = wall
        self.castle = castle
        self.university = university

    def getBuilding(self, buildingType: BuildingType):
        if buildingType == BuildingType.TOWNCENTER:
            return self.towncenter
        elif buildingType == BuildingType.MARKET:
            return self.market
        elif buildingType == BuildingType.BARRACKS:
            return self.barracks
        elif buildingType == BuildingType.WALL:
            return self.wall
        elif buildingType == BuildingType.CASTLE:
            return self.castle
        elif buildingType == BuildingType.UNIVERSITY:
            return self.university

    def add(self, buildingType: BuildingType, amount: int = 1):
        if buildingType == BuildingType.TOWNCENTER:
            self.towncenter += amount
        elif buildingType == BuildingType.MARKET:
            self.market += amount
        elif buildingType == BuildingType.BARRACKS:
            self.barracks += amount
        elif buildingType == BuildingType.WALL:
            self.wall += amount
        elif buildingType == BuildingType.CASTLE:
            self.castle += amount
        elif buildingType == BuildingType.UNIVERSITY:
            self.university += amount

    def remove(self, buidingType: BuildingType, amount: int = 1):
        self.add(buidingType, -amount)

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
