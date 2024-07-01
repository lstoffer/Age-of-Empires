from Field import Field

class Fields:
    def __init__(self, fields: dict) -> None:
        self.fields = {}
        for key, value in fields:
            self.fields[int(key)] = Field.from_dict(value)

    def __getitem__(self, key: int):
        return self.fields[key]