from Nation import Nation
from utils.NationType import NationType


class Nations:
    def __init__(self, britons: Nation, vikings: Nation, chinese: Nation, mongols: Nation) -> None:
        self.britons = britons
        self.vikings = vikings
        self.chinese = chinese
        self.mongols = mongols

    def getAll(self):
        return [self.britons, self.vikings, self.chinese, self. mongols]
    
    def getNation(self, nationType: NationType):
        if nationType == NationType.BRITONS:
            return self.britons
        elif nationType == NationType.VIKINGS:
            return self.vikings
        elif nationType == NationType.CHINESE:
            return self.chinese
        elif nationType == NationType.MONGOLS:
            return self.mongols

    def serialize(self):
        nations = {
            NationType.BRITONS.value: self.britons.serialize(),
            NationType.VIKINGS.value: self.vikings.serialize(),
            NationType.CHINESE.value: self.chinese.serialize(),
            NationType.MONGOLS.value: self.mongols.serialize()
        }
        return nations
