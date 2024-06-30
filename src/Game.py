from DataLoader import DataLoader
from Borders import Borders

class Game:
    def __init__(self) -> None:
        self.dataLoader = DataLoader()
        self.updates = self.dataLoader.updates
        self.borders = Borders(self.dataLoader.borders())

        