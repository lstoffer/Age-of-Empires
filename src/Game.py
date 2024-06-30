from DataLoader import DataLoader
from Borders import Borders
from Nation import Nation

class Game:
    def __init__(self) -> None:
        self.dataLoader = DataLoader()
        self.updates = self.dataLoader.updates
        self.borders = Borders(self.dataLoader.borders())

        self.britions = 