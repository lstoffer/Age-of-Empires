from PyQt5.QtWidgets import QApplication
import sys
from Game import Game
from GameGUI import GameGUI


class GamePresenter:
    def __init__(self) -> None:
        self.model = Game()
        app = QApplication(sys.argv)
        self.gui = GameGUI()

        self.model.displayError.connect(self.gui.displayError)
        self.model.displayInfo.connect(self.gui.displayInfo)

        self.gui.refresh_btn.clicked.connect(self.model.updateNations)
        self.model.updateNation.connect(self.gui.updateNation)

        self.gui.field_select_spinBox.valueChanged.connect(self.model.updateFields)
        self.model.updateField.connect(self.gui.updateField)

        self.gui.addResources.connect(self.model.addResources)
        self.gui.applyDividends.connect(self.model.applyResourceDividends)

        self.gui.moveVillagers.connect(self.model.moveVillagers)
        self.gui.developVillagers.connect(self.model.developVillagers)

        self.gui.buildBuilding.connect(self.model.buildBuilding)
        self.gui.destroyBuilding.connect(self.model.destroyBuilding)
        self.gui.buildWall.connect(self.model.buildWall)
        self.gui.destroyWall.connect(self.model.destroyWall)

        self.gui.stopGame.connect(self.model.stopGame)

        self.gui.updateAge.connect(self.model.updateAge)

        self.gui.developTroops.connect(self.model.developTroops)
        self.gui.moveTroops.connect(self.model.moveTroops)
        self.gui.attack.connect(self.model.attack)

        self.gui.trade.connect(self.model.trade)

        self.gui.applyUpdate.connect(self.model.applyUpdate)

        self.model.updateNations()
        
        try:
            self.gui.show()
            app.exec()

        except Exception:
            self.model.serialize()


GamePresenter()
