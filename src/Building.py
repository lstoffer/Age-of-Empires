import utils.Buildings as Buildings, utils.Nations as Nations

class Building:
    def __init__(self, nation: Nations, type: Buildings) -> None:
        self.nation = nation
        self.type = type
    
    def get_def(self):
        pass