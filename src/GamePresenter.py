from PyQt5.QtWidgets import QApplication
import sys
from Game import Game
from GameGUI import GameGUI

class GamePresenter:
    def __init__(self) -> None:
        self.model = Game()
        app = QApplication(sys.argv)
        self.gui = GameGUI()

        self.gui.refresh_btn.clicked.connect(self.model.updateNations)
        self.model.updateNation.connect(self.gui.updateNation)

        self.gui.addRessources.connect(self.model.addRessources)
        self.gui.applyDividends.connect(self.model.applyRessourceDividends)

        self.gui.moveVillagers.connect(self.model.moveVillagers)
        self.gui.developVillagers.connect(self.model.developVillagers)

        self.gui.buildBuilding.connect(self.model.buildBuilding)
        self.gui.destroyBuilding.connect(self.model.destroyBuilding)

        self.gui.stopGame.connect(self.model.stopGame)

        self.gui.updateAge.connect(self.model.updateAge)

        try:
            self.gui.show()
            app.exec()

            self.model.updateNations()
        except Exception:
            self.model.serialize()


GamePresenter()
