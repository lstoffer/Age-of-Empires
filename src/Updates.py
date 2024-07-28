from Update import Update
from utils.NationType import NationType
from utils.UpdateType import UpdateType


class Updates:
    def __init__(self, updates: dict) -> None:
        self.updates = {
            UpdateType(key): Update.from_dict(value) for key, value in updates.items()
        }

    def getUpdate(self, updateType: UpdateType) -> Update:
        return self.updates[updateType]