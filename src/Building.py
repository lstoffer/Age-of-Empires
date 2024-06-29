from utils.Ressources import Ressources


class Building:
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
