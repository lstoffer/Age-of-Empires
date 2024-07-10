from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QPushButton, QSpinBox, QComboBox
from ui import GameUI
from Nation import Nation
from utils.NationType import NationType
from utils.Ressources import Ressources
from utils.BuildingType import BuildingType

class GameGUI(QtWidgets.QMainWindow, GameUI.Ui_MainWindow):
    
    stopGame = pyqtSignal()
    
    # Ressources
    addRessources = pyqtSignal(Ressources, NationType)
    applyDividends = pyqtSignal(int)

    # Villagers
    moveVillagers = pyqtSignal(NationType, int, int, int)
    developVillagers = pyqtSignal(NationType, int, int)

    # Buildings
    buildBuilding = pyqtSignal(NationType, int, BuildingType)
    destroyBuilding = pyqtSignal(NationType, int, BuildingType)

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.setupNationSelect()
        self.setupBuildingSelect()
        # Ressources
        self.ressources_add_btn.clicked.connect(self.onRssourcesAddClick)
        self.ressources_sub_btn.clicked.connect(self.onRessourcesSubClick)
        self.ressources_dividends_btn.clicked.connect(self.onRessourceDividendsClick)

        # Villagers
        self.villagers_move_btn.clicked.connect(self.onVillagersMoveClick)
        self.villagers_develop_btn.clicked.connect(self.onVillagersDevelopClick)

        #Buildings
        self.buildings_build_btn.clicked.connect(self.onBuildingsBuildClick)
        self.buildings_destroy_btn.clicked.connect(self.onBuildingsDestroyClick)
        

    def closeEvent(self, event):
        super().closeEvent(event)
        self.stopGame.emit()

    def setupNationSelect(self):
        self.nation_select_comboBox.addItem('Briten', 'britons')
        self.nation_select_comboBox.addItem('Wikinger', 'vikings')
        self.nation_select_comboBox.addItem('Chinesen', 'chinese')
        self.nation_select_comboBox.addItem('Mongolen', 'mongols')

    def setupBuildingSelect(self):
        self.buildings_type_comboBox.addItem('Dorfzentrum', 'towncenter')
        self.buildings_type_comboBox.addItem('Markt', 'market')
        self.buildings_type_comboBox.addItem('Kaserne', 'barracks')
        self.buildings_type_comboBox.addItem('Wall', 'wall')
        self.buildings_type_comboBox.addItem('Burg', 'Castle')
        self.buildings_type_comboBox.addItem('Universität', 'university')
    
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

    def onVillagersMoveClick(self):
        nation = NationType(self.nation_select_comboBox.currentData())
        amount = self.villagers_move_amount_spinBox.value()
        fromField = self.villagers_move_from_spinBox.value()
        toField = self.villagers_move_to_spinBox.value()
        self.moveVillagers(nation, amount, fromField, toField)

    def onVillagersDevelopClick(self):
        nation = NationType(self.nation_select_comboBox.currentData())
        amount = self.villagers_develop_amount_spinBox.value()
        field = self.villagers_develop_field_spinBox.value()
        self.developVillagers(nation, field, amount)

    def onBuildingsBuildClick(self):
        nation = NationType(self.nation_select_comboBox.currentData())
        field = self.buildings_field_select_spinBox.value()
        buildingType = BuildingType(self.buildings_type_comboBox.currentData())
        self.buildBuilding(nation, field, buildingType)

    def onBuildingsDestroyClick(self):
        nation = NationType(self.nation_select_comboBox.currentData())
        field = self.buildings_field_select_spinBox.value()
        buildingType = BuildingType(self.buildings_type_comboBox.currentData())
        self.destroyBuilding(nation, field, buildingType)

    
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

    def updateVikings(self, nation: Nation):
        self.vikings_points_label = nation.getPoints()
        self.vikings_age_label = nation.age.value()
        self.vikings_food_label = nation.ressources.food
        self.vikings_wood_label = nation.ressources.wood
        self.vikings_stone_label = nation.ressources.stone
        self.vikings_gold_label = nation.ressources.gold
        self.vikings_archer_label = nation.troops.archer
        self.vikings_infantry_label = nation.troops.infantry
        self.vikings_cavalry_label = nation.troops.cavalry
        self.vikings_siege_label = nation.troops.siege
        self.vikings_towncenter_label = nation.buildings.towncenter
        self.vikings_market_label = nation.buildings.market
        self.vikings_barracks_label = nation.buildings.barracks
        self.vikings_wall_label = nation.buildings.wall
        self.vikings_castle_label = nation.buildings.castle
        self.vikings_universtity_label = nation.buildings.university

        for update in nation.updates:
            self.vikings_updates_list.addItem(update.value())
        for field in nation.fields:
            self.vikings_fields_list.addItem(field)

    def updateChinese(self, nation: Nation):
        self.chinese_points_label = nation.getPoints()
        self.chinese_age_label = nation.age.value()
        self.chinese_food_label = nation.ressources.food
        self.chinese_wood_label = nation.ressources.wood
        self.chinese_stone_label = nation.ressources.stone
        self.chinese_gold_label = nation.ressources.gold
        self.chinese_archer_label = nation.troops.archer
        self.chinese_infantry_label = nation.troops.infantry
        self.chinese_cavalry_label = nation.troops.cavalry
        self.chinese_siege_label = nation.troops.siege
        self.chinese_towncenter_label = nation.buildings.towncenter
        self.chinese_market_label = nation.buildings.market
        self.chinese_barracks_label = nation.buildings.barracks
        self.chinese_wall_label = nation.buildings.wall
        self.chinese_castle_label = nation.buildings.castle
        self.chinese_universtity_label = nation.buildings.university

        for update in nation.updates:
            self.chinese_updates_list.addItem(update.value())
        for field in nation.fields:
            self.chinese_fields_list.addItem(field)

    def updateMongols(self, nation: Nation):
        self.mongols_points_label = nation.getPoints()
        self.mongols_age_label = nation.age.value()
        self.mongols_food_label = nation.ressources.food
        self.mongols_wood_label = nation.ressources.wood
        self.mongols_stone_label = nation.ressources.stone
        self.mongols_gold_label = nation.ressources.gold
        self.mongols_archer_label = nation.troops.archer
        self.mongols_infantry_label = nation.troops.infantry
        self.mongols_cavalry_label = nation.troops.cavalry
        self.mongols_siege_label = nation.troops.siege
        self.mongols_towncenter_label = nation.buildings.towncenter
        self.mongols_market_label = nation.buildings.market
        self.mongols_barracks_label = nation.buildings.barracks
        self.mongols_wall_label = nation.buildings.wall
        self.mongols_castle_label = nation.buildings.castle
        self.mongols_universtity_label = nation.buildings.university

        for update in nation.updates:
            self.mongols_updates_list.addItem(update.value())
        for field in nation.fields:
            self.mongols_fields_list.addItem(field)
