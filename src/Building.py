from utils.Ressources import Ressources


class Building:
    '''
    Class that represents one building unit.
    '''
    def __init__(self, cost: Ressources, defence: int, structure: int, points: int) -> None:
        self.cost = cost
        self.defence = defence
        self.structure = structure
        self.points = points

    @classmethod
    def from_dict(cls, dict):
        cost = Ressources.from_dict(dict['costs'])
        defence = dict['defence']
        structure = dict['structure']
        points = dict['points']
        return cls(cost, defence, structure, points)
    
    def __add__(self, other):
        if isinstance(other, Building):
            return Building(self.cost + other.cost,
                            self.defence + other.defence,
                            self.structure + other.structure,
                            self.points + other.points)
        return NotImplemented
