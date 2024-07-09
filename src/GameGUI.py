from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import pyqtSlot
from ui import GameUI
from Nation import Nation
from utils.NationType import NationType

class GameGUI(QtWidgets.QMainWindow, GameUI.Ui_MainWindow):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setupUi(self)

    @pyqtSlot(NationType, Nation)
    def updateNation(self, nationType: NationType, nation: Nation):
        if nationType == NationType.BRITONS:
            self.updateBritions(nation)
        elif nationType == NationType.VIKINGS:
            self.updateVikings(nation)
        elif nationType == NationType.CHINESE:
            self.updateChinese(nation)
        elif nationType == NationType.MONGOLS:
            self.updateMongols(nation)

    def updateBritions(self, nation: Nation):
        self.britons_points_label = nation.getPoints()
        self.britons_age_label = nation.age.value()
        self.britons_food_label = nation.ressources.food
        self.britons_wood_label = nation.ressources.wood
        self.britons_stone_label = nation.ressources.stone
        self.britons_gold_label = nation.ressources.gold
        self.britons_archer_label = nation.troops.archer
        self.britons_infantry_label = nation.troops.infantry
        self.britons_cavalry_label = nation.troops.cavalry
        self.britons_siege_label = nation.troops.siege
        self.britons_towncenter_label = nation.buildings.towncenter
        self.britons_market_label = nation.buildings.market
        self.britons_barracks_label = nation.buildings.barracks
        self.britons_wall_label = nation.buildings.wall
        self.britons_castle_label = nation.buildings.castle
        self.britons_universtity_label = nation.buildings.university

        for update in nation.updates:
            self.britons_updates_list.addItem(update.value())
        for field in nation.fields:
            self.britons_fields_list.addItem(field)
