from utils.RessourceType import RessourceType
class Ressources:
    def __init__(self, food: int, wood: int, stone: int, gold: int) -> None:
        self.food = food
        self.wood = wood
        self.stone = stone
        self.gold = gold

    @classmethod
    def from_dict(cls, dict):
        food = dict[RessourceType.FOOD]
        wood = dict[RessourceType.WOOD]
        stone = dict[RessourceType.STONE]
        gold = dict[RessourceType.GOLD]
        return cls(food, wood, stone, gold)
    
    def __add__(self, other):
        if isinstance(other, Ressources):
            return Ressources(self.food + other.food,
                              self.wood + other.wood,
                              self.stone + other.stone,
                              self.gold + other.gold)
