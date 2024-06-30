from Building import Building

class BuildingInstances:
    def __init__(self, towncenter: Building = None, market: Building = None, barracks: Building = None, wall: Building = None, castle: Building = None, university: Building = None) -> None:
        self.towncenter = towncenter
        self.market = market
        self.barracks = barracks
        self.wall = wall
        self.castle = castle
        self.university = university