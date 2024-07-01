from Field import Field

class Fields:
    def __init__(self, fields: dict) -> None:
        self.fields = {int(key): Field.from_dict(value) for key, value in fields.items()}

    def __getitem__(self, key: int):
        return self.fields[key]
    
    def serialize(self):
        fields = {str(key): value.serialize() for key, value in self.fields.items()}