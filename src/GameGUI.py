from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QPushButton, QSpinBox, QComboBox
from ui import GameUI
from Nation import Nation
from utils.NationType import NationType
from utils.Ressources import Ressources

class GameGUI(QtWidgets.QMainWindow, GameUI.Ui_MainWindow):
    
    addRessources = pyqtSignal(Ressources, NationType)
    applyDividends = pyqtSignal(int)

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.ressources_add_btn.clicked.connect(self.onRssourcesAddClick)
        self.ressources_sub_btn.clicked.connect(self.onRessourcesSubClick)
        self.ressources_dividends_btn.clicked.connect(self.onRessourceDividendsClick)

    def setupNationSelect(self):
        self.nation_select_comboBox.addItem('Briten', 'britons')
        self.nation_select_comboBox.addItem('Wikinger', 'vikings')
        self.nation_select_comboBox.addItem('Chinesen', 'chinese')
        self.nation_select_comboBox.addItem('Mongolen', 'mongols')
    
    def onRssourcesAddClick(self):
        food = self.food_add_sub_spinBox.value()
        wood = self.wood_add_sub_spinBox.value()
        stone = self.stone_add_sub_spinBox.value()
        gold = self.stone_add_sub_spinBox.value()
        nation = NationType(self.nation_select_comboBox.currentData())
        ressources = Ressources(food, wood, stone, gold)
        self.addRessources.emit(ressources, nation)

    def onRessourcesSubClick(self):
        food = self.food_add_sub_spinBox.value()
        wood = self.wood_add_sub_spinBox.value()
        stone = self.stone_add_sub_spinBox.value()
        gold = self.stone_add_sub_spinBox.value()
        nation = NationType(self.nation_select_comboBox.currentData())
        ressources = Ressources(-food, -wood, -stone, -gold)
        self.addRessources.emit(ressources, nation)

    def onRessourceDividendsClick(self):
        rounds = self.ressources_dividends_spinBox.value()
        nation = NationType(self.nation_select_comboBox.currentData())
        self.applyDividends.emit(rounds)

    
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
