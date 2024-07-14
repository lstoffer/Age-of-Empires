from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QPushButton, QSpinBox, QComboBox
from ui import GameUI
from Nation import Nation
from Field import Field
from utils.NationType import NationType
from utils.Ressources import Ressources
from utils.BuildingType import BuildingType

class GameGUI(QtWidgets.QMainWindow, GameUI.Ui_MainWindow):
    
    stopGame = pyqtSignal()
    
    # Ressources
    addRessources = pyqtSignal(NationType, Ressources)
    applyDividends = pyqtSignal(int)

    # Villagers
    moveVillagers = pyqtSignal(NationType, int, int, int)
    developVillagers = pyqtSignal(NationType, int, int)

    # Buildings
    buildBuilding = pyqtSignal(NationType, int, BuildingType)
    destroyBuilding = pyqtSignal(NationType, int, BuildingType)

    updateAge = pyqtSignal(NationType)

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

        # Ages
        self.ages_update_btn.clicked.connect(self.onAgeUpdateClick)
        

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
        gold = self.gold_add_sub_spinBox.value()
        nation = NationType(self.nation_select_comboBox.currentData())
        ressources = Ressources(food, wood, stone, gold)
        self.addRessources.emit(nation, ressources)

    def onRessourcesSubClick(self):
        food = self.food_add_sub_spinBox.value()
        wood = self.wood_add_sub_spinBox.value()
        stone = self.stone_add_sub_spinBox.value()
        gold = self.gold_add_sub_spinBox.value()
        nation = NationType(self.nation_select_comboBox.currentData())
        ressources = Ressources(-food, -wood, -stone, -gold)
        self.addRessources.emit(nation, ressources)

    def onRessourceDividendsClick(self):
        rounds = self.ressources_dividends_spinBox.value()
        nation = NationType(self.nation_select_comboBox.currentData())
        self.applyDividends.emit(rounds)

    def onVillagersMoveClick(self):
        nation = NationType(self.nation_select_comboBox.currentData())
        amount = self.villagers_move_amount_spinBox.value()
        fromField = self.villagers_move_from_spinBox.value()
        toField = self.villagers_move_to_spinBox.value()
        self.moveVillagers.emit(nation, amount, fromField, toField)

    def onVillagersDevelopClick(self):
        nation = NationType(self.nation_select_comboBox.currentData())
        amount = self.villagers_develop_amount_spinBox.value()
        field = self.villagers_develop_field_spinBox.value()
        self.developVillagers.emit(nation, field, amount)

    def onBuildingsBuildClick(self):
        nation = NationType(self.nation_select_comboBox.currentData())
        field = self.buildings_field_select_spinBox.value()
        buildingType = BuildingType(self.buildings_type_comboBox.currentData())
        self.buildBuilding.emit(nation, field, buildingType)

    def onBuildingsDestroyClick(self):
        nation = NationType(self.nation_select_comboBox.currentData())
        field = self.buildings_field_select_spinBox.value()
        buildingType = BuildingType(self.buildings_type_comboBox.currentData())
        self.destroyBuilding(nation, field, buildingType)

    def onAgeUpdateClick(self):
        nation = NationType(self.nation_select_comboBox.currentData())
        self.updateAge.emit(nation)

    @pyqtSlot(Field)
    def updateField(self, field: Field):
        self.field_ressource_label.setText(field.ressource.value)
        self.field_nation_label.setText(field.nation.value)
        self.field_villager_amount_label.setText(str(field.villagers))
        self.field_archer_amount_label.setText(str(field.troops.archer))
        self.field_infantry_amount_label.setText(str(field.troops.infantry))
        self.field_cavalry_amount_label.setText(str(field.troops.cavalry))
        self.field_siege_amount_label.setText(str(field.troops.siege))
        self.field_towncenter_amount_label.setText(str(field.buildings.towncenter))
        self.field_market_amount_label.setText(str(field.buildings.market))
        self.field_barracks_amount_label.setText(str(field.buildings.barracks))
        self.field_wall_amount_label.setText(str(field.buildings.wall))
        self.field_castle_amount_label.setText(str(field.buildings.castle))
        self.field_university_amount_label.setText(str(field.buildings.university))
    
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
        self.britons_points_label.setText(str(nation.getPoints())) 
        self.britons_age_label.setText(str(nation.age.value))
        self.britons_villagers_label.setText(str(nation.villagers))
        self.britons_food_label.setText(str(nation.ressources.food))
        self.britons_wood_label.setText(str(nation.ressources.wood))
        self.britons_stone_label.setText(str(nation.ressources.stone))
        self.britons_gold_label.setText(str(nation.ressources.gold))
        self.britons_archer_label.setText(str(nation.troops.archer))
        self.britons_infantry_label.setText(str(nation.troops.infantry))
        self.britons_cavalry_label.setText(str(nation.troops.cavalry))
        self.britons_siege_label.setText(str(nation.troops.siege))
        self.britons_towncenter_label.setText(str(nation.buildings.towncenter))
        self.britons_market_label.setText(str(nation.buildings.market))
        self.britons_barracks_label.setText(str(nation.buildings.barracks))
        self.britons_wall_label.setText(str(nation.buildings.wall))
        self.britons_castle_label.setText(str(nation.buildings.castle))
        self.britons_universtity_label.setText(str(nation.buildings.university))

        for update in nation.updates:
            self.britons_updates_list.addItem(update.value)
        for field in nation.fields:
            self.britons_fields_list.addItem(str(field))

    def updateVikings(self, nation: Nation):
        self.vikings_points_label.setText(str(nation.getPoints())) 
        self.vikings_age_label.setText(str(nation.age.value))
        self.vikings_villagers_label.setText(str(nation.villagers))
        self.vikings_food_label.setText(str(nation.ressources.food))
        self.vikings_wood_label.setText(str(nation.ressources.wood))
        self.vikings_stone_label.setText(str(nation.ressources.stone))
        self.vikings_gold_label.setText(str(nation.ressources.gold))
        self.vikings_archer_label.setText(str(nation.troops.archer))
        self.vikings_infantry_label.setText(str(nation.troops.infantry))
        self.vikings_cavalry_label.setText(str(nation.troops.cavalry))
        self.vikings_siege_label.setText(str(nation.troops.siege))
        self.vikings_towncenter_label.setText(str(nation.buildings.towncenter))
        self.vikings_market_label.setText(str(nation.buildings.market))
        self.vikings_barracks_label.setText(str(nation.buildings.barracks))
        self.vikings_wall_label.setText(str(nation.buildings.wall))
        self.vikings_castle_label.setText(str(nation.buildings.castle))
        self.vikings_universtity_label.setText(str(nation.buildings.university))

        for update in nation.updates:
            self.vikings_updates_list.addItem(update.value)
        for field in nation.fields:
            self.vikings_fields_list.addItem(str(field))

    def updateChinese(self, nation: Nation):
        self.chinese_points_label.setText(str(nation.getPoints())) 
        self.chinese_age_label.setText(str(nation.age.value))
        self.chinese_villagers_label.setText(str(nation.villagers))
        self.chinese_food_label.setText(str(nation.ressources.food))
        self.chinese_wood_label.setText(str(nation.ressources.wood))
        self.chinese_stone_label.setText(str(nation.ressources.stone))
        self.chinese_gold_label.setText(str(nation.ressources.gold))
        self.chinese_archer_label.setText(str(nation.troops.archer))
        self.chinese_infantry_label.setText(str(nation.troops.infantry))
        self.chinese_cavalry_label.setText(str(nation.troops.cavalry))
        self.chinese_siege_label.setText(str(nation.troops.siege))
        self.chinese_towncenter_label.setText(str(nation.buildings.towncenter))
        self.chinese_market_label.setText(str(nation.buildings.market))
        self.chinese_barracks_label.setText(str(nation.buildings.barracks))
        self.chinese_wall_label.setText(str(nation.buildings.wall))
        self.chinese_castle_label.setText(str(nation.buildings.castle))
        self.chinese_universtity_label.setText(str(nation.buildings.university))

        for update in nation.updates:
            self.chinese_updates_list.addItem(update.value)
        for field in nation.fields:
            self.chinese_fields_list.addItem(str(field))

    def updateMongols(self, nation: Nation):
        self.mongols_points_label.setText(str(nation.getPoints())) 
        self.mongols_age_label.setText(str(nation.age.value))
        self.mongols_villagers_label.setText(str(nation.villagers))
        self.mongols_food_label.setText(str(nation.ressources.food))
        self.mongols_wood_label.setText(str(nation.ressources.wood))
        self.mongols_stone_label.setText(str(nation.ressources.stone))
        self.mongols_gold_label.setText(str(nation.ressources.gold))
        self.mongols_archer_label.setText(str(nation.troops.archer))
        self.mongols_infantry_label.setText(str(nation.troops.infantry))
        self.mongols_cavalry_label.setText(str(nation.troops.cavalry))
        self.mongols_siege_label.setText(str(nation.troops.siege))
        self.mongols_towncenter_label.setText(str(nation.buildings.towncenter))
        self.mongols_market_label.setText(str(nation.buildings.market))
        self.mongols_barracks_label.setText(str(nation.buildings.barracks))
        self.mongols_wall_label.setText(str(nation.buildings.wall))
        self.mongols_castle_label.setText(str(nation.buildings.castle))
        self.mongols_universtity_label.setText(str(nation.buildings.university))

        for update in nation.updates:
            self.mongols_updates_list.addItem(update.value)
        for field in nation.fields:
            self.mongols_fields_list.addItem(str(field))
        