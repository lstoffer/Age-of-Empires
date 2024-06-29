from utils.Ressources import Ressources


class Troop:
    def __init__(self, cost: Ressources, defence: int, attack: int, points: int) -> None:
        self.cost = cost
        self.defence = defence
        self.attack = attack
        self.points = points

    @classmethod
    def from_dict(cls, dict):
        cost = Ressources.from_dict(dict['costs'])
        defence = dict['defence']
        attack = dict['attack']
        points = dict['points']
        return cls(cost, defence, attack, points)
