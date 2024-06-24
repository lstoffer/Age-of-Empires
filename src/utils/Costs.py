from dataclasses import dataclass

@dataclass
class Cost:
    food: int
    wood: int
    stone: int
    gold: int

    @classmethod
    def from_dict(cls, dict):
        food = dict['food']
        wood = dict['wood']
        stone = dict['stone']
        gold = dict['gold']
        return cls(food, wood, stone, gold)