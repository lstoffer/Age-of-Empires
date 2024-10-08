from utils.Ressources import Ressources


class Villager:
    '''
    Class that represents one villager unit.
    '''
    def __init__(self, cost: Ressources, profit: Ressources, defence: int, points: int) -> None:
        self.cost = cost
        self.profit = profit
        self.defence = defence
        self.points = points

    @classmethod
    def from_dict(cls, dict):
        cost = Ressources.from_dict(dict['costs'])
        profit = Ressources.from_dict(dict['profits'])
        defence = dict['defence']
        points = dict['points']
        return cls(cost, profit, defence, points)
    
    def __add__(self, other):
        if isinstance(other, Villager):
            return Villager(self.cost + other.cost,
                            self.profit + other.profit,
                            self.defence + other.defence,
                            self.points + other.points)
        return NotImplemented
