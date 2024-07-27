from Update import Update
from utils.NationType import NationType
from utils.UpdateType import UpdateType


class Updates:
    def __init__(self, updates: dict) -> None:
        self.updates = dict()

        self.updates[NationType.BRITONS] = {
            UpdateType(key): Update.from_dict(value) for key, value in updates[NationType.BRITONS.value].items()
        }
        self.updates[NationType.VIKINGS] = {
            UpdateType(key): Update.from_dict(value) for key, value in updates[NationType.VIKINGS.value].items()
        }
        self.updates[NationType.CHINESE] = {
            UpdateType(key): Update.from_dict(value) for key, value in updates[NationType.CHINESE.value].items()
        }
        self.updates[NationType.MONGOLS] = {
            UpdateType(key): Update.from_dict(value) for key, value in updates[NationType.MONGOLS.value].items()
        }

    def getUpdates(self, nationType: NationType = None) -> dict
        if nationType:
            return self.updates[nationType]
        else:
            return self.updates

    def getUpdate(self, nationType: NationType, updateType: UpdateType) -> Update:
        return self.updates[nationType][updateType]