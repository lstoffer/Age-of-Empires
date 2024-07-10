from PyQt5.QtWidgets import QApplication
import sys
from Game import Game
from GameGUI import GameGUI

class GamePresenter:
    def __init__(self) -> None:
        self.model = Game()
        app = QApplication(sys.argv)
        self.gui = GameGUI()


        self.gui.addRessources.connect(self.model.addRessources)
        self.gui.applyDividends.connect(self.model.applyRessourceDividends)


        self.gui.show()
        app.exec()

GamePresenter()