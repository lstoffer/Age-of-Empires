from dataclasses import dataclass

@dataclass
class Cost:
    gold: int
    wood: int
    food: int
    stone: int