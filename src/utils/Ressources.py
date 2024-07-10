from utils.RessourceType import RessourceType
class Ressources:
    def __init__(self, food: int, wood: int, stone: int, gold: int) -> None:
        self.food = food
        self.wood = wood
        self.stone = stone
        self.gold = gold

    @classmethod
    def from_dict(cls, dict):
        food = dict[RessourceType.FOOD.value]
        wood = dict[RessourceType.WOOD.value]
        stone = dict[RessourceType.STONE.value]
        gold = dict[RessourceType.GOLD.value]
        return cls(food, wood, stone, gold)
    
    def add(self, ressourceType: RessourceType, amount: int):
        if ressourceType == RessourceType.FOOD:
            self.food += amount
        elif ressourceType == RessourceType.WOOD:
            self.wood += amount
        elif ressourceType == RessourceType.STONE:
            self.stone += amount
        elif ressourceType == RessourceType.GOLD:
            self.gold += amount

    def get(self, ressourceType: RessourceType):
        if ressourceType == RessourceType.FOOD:
            return self.food
        elif ressourceType == RessourceType.WOOD:
            return self.wood
        elif ressourceType == RessourceType.STONE:
            return self.stone
        elif ressourceType == RessourceType.GOLD:
            return self.gold
    
    def __add__(self, other):
        if isinstance(other, Ressources):
            return Ressources(self.food + other.food,
                              self.wood + other.wood,
                              self.stone + other.stone,
                              self.gold + other.gold)
        
    def __mul__(self, scalar):
        if isinstance(scalar, int):
            return Ressources(self.food * scalar,
                              self.wood * scalar,
                              self.stone * scalar,
                              self.gold * scalar)
        
    def serialize(self) -> dict:
        ressourcesData = {}
        ressourcesData[RessourceType.FOOD.value] = self.food
        ressourcesData[RessourceType.WOOD.value] = self.wood
        ressourcesData[RessourceType.STONE.value] = self.stone
        ressourcesData[RessourceType.GOLD.value] = self.gold
        return ressourcesData
