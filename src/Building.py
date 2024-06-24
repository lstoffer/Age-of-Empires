import utils.Buildings as Buildings
import utils.Nations as Nations
import DataLoader
from utils.Costs import Cost


class Building:
    def __init__(self, nation: Nations, type: Buildings) -> None:
        self.nation = nation
        self.type = type
        initialData = DataLoader.load_building_data(building_type=type, nation=nation)
        self.structure = initialData['structure']
        self.defence = initialData['defence']
        self.cost = Cost.from_dict(initialData['costs'])

    def get_def(self):
        pass
