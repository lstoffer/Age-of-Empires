from Field import Field


class Fields:
    '''
    Container class for all fields on the board
    '''
    def __init__(self, fields: dict) -> None:
        self.fields = {int(key): Field.from_dict(value) for key, value in fields.items()}

    def __getitem__(self, key: int) -> Field:
        return self.fields[key]

    def fieldNumbers(self):
        return list(self.fields.keys())

    def serialize(self):
        fields = {str(key): value.serialize() for key, value in self.fields.items()}
        return fields
