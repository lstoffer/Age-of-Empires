from utils.AgeType import AgeType


class Points:
    def __init__(self, ages: dict, field: int) -> None:
        self.ages = ages
        self.field = field

    @classmethod
    def from_dict(cls, dict: dict):
        ages = {AgeType(key): value for key, value in dict['ages'].items()}
        field = dict['field']
        return cls(ages, field)

    def serialize(self):
        ages = {key.value: point for key, point in self.ages.items()}
        points = {
            'ages': ages,
            'field': self.field
        }
        return points
