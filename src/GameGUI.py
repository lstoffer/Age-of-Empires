from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QPushButton, QSpinBox, QComboBox, QMessageBox
from ui import GameUI
from Nation import Nation
from Field import Field
from utils.TroopType import TroopType
from utils.NationType import NationType
from utils.Ressources import Ressources
from utils.BuildingType import BuildingType
from utils.RessourceType import RessourceType
from utils.UpdateType import UpdateType
from Points import Points


class GameGUI(QtWidgets.QMainWindow, GameUI.Ui_MainWindow):
    
    stopGame = pyqtSignal()
    
    # Resources
    addResources = pyqtSignal(NationType, Ressources)
    applyDividends = pyqtSignal(int)

    # Villagers
    moveVillagers = pyqtSignal(NationType, int, int, int)
    developVillagers = pyqtSignal(NationType, int, int)

    # Buildings
    buildBuilding = pyqtSignal(NationType, int, BuildingType)
    destroyBuilding = pyqtSignal(NationType, int, BuildingType)
    buildWall = pyqtSignal(NationType, int, int)
    destroyWall = pyqtSignal(int, int)

    updateAge = pyqtSignal(NationType)

    developTroops = pyqtSignal(NationType, TroopType, int, int)
    moveTroops = pyqtSignal(NationType, int, int, int, int, int, int)
    attack = pyqtSignal(int, int)

    trade = pyqtSignal(NationType, RessourceType, RessourceType, int, int)

    applyUpdate = pyqtSignal(NationType, UpdateType)

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.setupNationSelect()
        self.setupBuildingSelect()
        self.setupTroopTypeSelect()
        self.setupTradeResourceSelect()
        self.setupUpdateSelect()

        # Resources
        self.ressources_add_btn.clicked.connect(self.onResourcesAddClick)
        self.ressources_sub_btn.clicked.connect(self.onResourcesSubClick)
        self.ressources_dividends_btn.clicked.connect(self.onResourceDividendsClick)

        # Villagers
        self.villagers_move_btn.clicked.connect(self.onVillagersMoveClick)
        self.villagers_develop_btn.clicked.connect(self.onVillagersDevelopClick)

        # Buildings
        self.buildings_build_btn.clicked.connect(self.onBuildingsBuildClick)
        self.buildings_destroy_btn.clicked.connect(self.onBuildingsDestroyClick)
        self.building_wall_build_btn.clicked.connect(self.onBuildingsWallBuildClick)
        self.building_wall_destroy_btn.clicked.connect(self.onBuildingsWallDestroyClick)

        # Ages
        self.ages_update_btn.clicked.connect(self.onAgeUpdateClick)

        # Troops
        self.troops_develop_btn.clicked.connect(self.onTroopsDevelopClick)
        self.troops_move_btn.clicked.connect(self.onTroopMoveClick)
        self.troops_attack_btn.clicked.connect(self.onAttackClick)

        # Trade
        self.trade_from_amount_spinBox.valueChanged.connect(self.tradeToAmountUpdate)
        self.trade_btn.clicked.connect(self.onTradeClick)

        # Updates
        self.update_apply_btn.clicked.connect(self.onUpdateApplyClick)

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
        self.buildings_type_comboBox.addItem('Burg', 'castle')
        self.buildings_type_comboBox.addItem('Universität', 'university')

    def setupTroopTypeSelect(self):
        self.troops_develop_typ_comboBox.addItem('Infanterie', 'infantry')
        self.troops_develop_typ_comboBox.addItem('Bogenschützen', 'archer')
        self.troops_develop_typ_comboBox.addItem('Kavallerie', 'cavalry')
        self.troops_develop_typ_comboBox.addItem('Belagerungswaffen', 'siege')

    def setupTradeResourceSelect(self):
        self.trade_from_comboBox.addItem('Nahrung', 'food')
        self.trade_from_comboBox.addItem('Holz', 'wood')
        self.trade_from_comboBox.addItem('Stein', 'stone')
        self.trade_from_comboBox.addItem('Gold', 'gold')
        self.trade_to_comboBox.addItem('Nahrung', 'food')
        self.trade_to_comboBox.addItem('Holz', 'wood')
        self.trade_to_comboBox.addItem('Stein', 'stone')
        self.trade_to_comboBox.addItem('Gold', 'gold')

    def setupUpdateSelect(self):
        self.update_apply_select_comboBox.addItem('Dorfbewohner I', 'wheel')
        self.update_apply_select_comboBox.addItem('Dorfbewohner II', 'trade-cart')
        self.update_apply_select_comboBox.addItem('Infanterie I', 'short-swordsman')
        self.update_apply_select_comboBox.addItem('Infanterie II', 'long-swordsman')
        self.update_apply_select_comboBox.addItem('Kavallerie I', 'heavy-cavalry')
        self.update_apply_select_comboBox.addItem('Kavallerie II', 'war-elephant')
        self.update_apply_select_comboBox.addItem('Bogenschütze I', 'improved-bowman')
        self.update_apply_select_comboBox.addItem('Bogenschütze II', 'composite-bowman')
        self.update_apply_select_comboBox.addItem('Truppen I', 'centurion')
        self.update_apply_select_comboBox.addItem('Truppen II', 'legionary')
        self.update_apply_select_comboBox.addItem('Belagerung I', 'stone-thrower')
        self.update_apply_select_comboBox.addItem('Belagerung II', 'trebuchet')
        self.update_apply_select_comboBox.addItem('Goldmine I', 'gold-mining')
        self.update_apply_select_comboBox.addItem('Goldmine II', 'gold-mining-ii')
        self.update_apply_select_comboBox.addItem('Steinbruch I', 'stone-mining')
        self.update_apply_select_comboBox.addItem('Steinburch II', 'stone-mining-ii')
        self.update_apply_select_comboBox.addItem('Nahrung I', 'domestication')
        self.update_apply_select_comboBox.addItem('Nahrung II', 'plow')
        self.update_apply_select_comboBox.addItem('Holz I', 'woodcutting')
        self.update_apply_select_comboBox.addItem('Holz II', 'artisanship')
        self.update_apply_select_comboBox.addItem('Wall I', 'big-wall')
        self.update_apply_select_comboBox.addItem('Wall II', 'stone-wall')
        self.update_apply_select_comboBox.addItem('Burg I', 'big-castle')
        self.update_apply_select_comboBox.addItem('Burg II', 'stone-castle')

    def onResourcesAddClick(self):
        food = self.food_add_sub_spinBox.value()
        wood = self.wood_add_sub_spinBox.value()
        stone = self.stone_add_sub_spinBox.value()
        gold = self.gold_add_sub_spinBox.value()
        nation = NationType(self.nation_select_comboBox.currentData())
        resources = Ressources(food, wood, stone, gold)
        self.addResources.emit(nation, resources)

    def onResourcesSubClick(self):
        food = self.food_add_sub_spinBox.value()
        wood = self.wood_add_sub_spinBox.value()
        stone = self.stone_add_sub_spinBox.value()
        gold = self.gold_add_sub_spinBox.value()
        nation = NationType(self.nation_select_comboBox.currentData())
        resources = Ressources(-food, -wood, -stone, -gold)
        self.addResources.emit(nation, resources)

    def onResourceDividendsClick(self):
        rounds = self.ressources_dividends_spinBox.value()
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

    def onBuildingsWallBuildClick(self):
        nation = NationType(self.nation_select_comboBox.currentData())
        field1 = self.buildings_wall_field1_select_spinBox.value()
        field2 = self.buildings_wall_field2_select_spinBox.value()
        self.buildWall.emit(nation, field1, field2)

    def onBuildingsWallDestroyClick(self):
        field1 = self.buildings_wall_field1_select_spinBox.value()
        field2 = self.buildings_wall_field2_select_spinBox.value()
        self.destroyWall.emit(field1, field2)

    def onAgeUpdateClick(self):
        nation = NationType(self.nation_select_comboBox.currentData())
        self.updateAge.emit(nation)

    def onTroopsDevelopClick(self):
        nationType = NationType(self.nation_select_comboBox.currentData())
        troopType = TroopType(self.troops_develop_typ_comboBox.currentData())
        amount = self.troops_develop_amount_spinBox.value()
        fieldNumber = self.troops_develop_field_spinBox.value()
        self.developTroops.emit(nationType, troopType, fieldNumber, amount)

    def onTroopMoveClick(self):
        nationType = NationType(self.nation_select_comboBox.currentData())
        archerAmount = self.troops_move_archer_amount_spinBox.value()
        infantryAmount = self.troops_move_infantry_amount_spinBox.value()
        cavalryAmount = self.troops_move_cavalry_amoutn_spinBox.value()
        siegeAmount = self.troops_move_siege_amount_spinBox.value()
        fromField = self.troops_move_from_spinBox.value()
        toField = self.troops_move_to_spinBox.value()
        self.moveTroops.emit(nationType, archerAmount, infantryAmount, cavalryAmount, siegeAmount, fromField, toField)

    def onAttackClick(self):
        fromField = self.troops_attack_from_spinBox.value()
        toField = self.troops_attack_to_spinBox.value()
        self.attack.emit(fromField, toField)

    def tradeToAmountUpdate(self, fromAmount: int):
        toAmount = int(fromAmount * 0.9)
        self.trade_to_amount_spinBox.setValue(toAmount)

    def onTradeClick(self):
        nationType = NationType(self.nation_select_comboBox.currentData())
        fromResourceType = RessourceType(self.trade_from_comboBox.currentData())
        toResourceType = RessourceType(self.trade_to_comboBox.currentData())
        fromAmount = self.trade_from_amount_spinBox.value()
        toAmount = self.trade_to_amount_spinBox.value()
        self.trade.emit(nationType, fromResourceType, toResourceType, fromAmount, toAmount)

    def onUpdateApplyClick(self):
        nationType = NationType(self.nation_select_comboBox.currentData())
        updateType = UpdateType(self.update_apply_select_comboBox.currentData())
        self.applyUpdate.emit(nationType, updateType)
 
    @pyqtSlot(str)
    def displayError(self, message: str):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Error")
        msg.setInformativeText(message)
        msg.setWindowTitle("Error")
        msg.exec_()

    @pyqtSlot(str)
    def displayInfo(self, message: str):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText('Info')
        msg.setInformativeText(message)
        msg.setWindowTitle("Info")
        msg.exec_()

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
    
    @pyqtSlot(NationType, Nation, Points)
    def updateNation(self, nationType: NationType, nation: Nation, points: Points):
        if nationType == NationType.BRITONS:
            self.updateBritons(nation, points)
        elif nationType == NationType.VIKINGS:
            self.updateVikings(nation, points)
        elif nationType == NationType.CHINESE:
            self.updateChinese(nation, points)
        elif nationType == NationType.MONGOLS:
            self.updateMongols(nation, points)

    def updateBritons(self, nation: Nation, points: Points):
        self.britons_points_label.setText(str(nation.getPoints(points))) 
        self.britons_age_label.setText(str(nation.age.value))
        self.britons_villagers_label.setText(str(nation.villagers))
        self.britons_food_label.setText(str(nation.resources.food))
        self.britons_wood_label.setText(str(nation.resources.wood))
        self.britons_stone_label.setText(str(nation.resources.stone))
        self.britons_gold_label.setText(str(nation.resources.gold))
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

        self.britons_updates_list.clear()
        self.britons_fields_list.clear()

        for update in nation.updates:
            self.britons_updates_list.addItem(update.value)
        for field in nation.fields:
            self.britons_fields_list.addItem(str(field))

    def updateVikings(self, nation: Nation, points: Points):
        self.vikings_points_label.setText(str(nation.getPoints(points))) 
        self.vikings_age_label.setText(str(nation.age.value))
        self.vikings_villagers_label.setText(str(nation.villagers))
        self.vikings_food_label.setText(str(nation.resources.food))
        self.vikings_wood_label.setText(str(nation.resources.wood))
        self.vikings_stone_label.setText(str(nation.resources.stone))
        self.vikings_gold_label.setText(str(nation.resources.gold))
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

        self.vikings_updates_list.clear()
        self.vikings_fields_list.clear()

        for update in nation.updates:
            self.vikings_updates_list.addItem(update.value)
        for field in nation.fields:
            self.vikings_fields_list.addItem(str(field))

    def updateChinese(self, nation: Nation, points: Points):
        self.chinese_points_label.setText(str(nation.getPoints(points))) 
        self.chinese_age_label.setText(str(nation.age.value))
        self.chinese_villagers_label.setText(str(nation.villagers))
        self.chinese_food_label.setText(str(nation.resources.food))
        self.chinese_wood_label.setText(str(nation.resources.wood))
        self.chinese_stone_label.setText(str(nation.resources.stone))
        self.chinese_gold_label.setText(str(nation.resources.gold))
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

        self.chinese_updates_list.clear()
        self.chinese_fields_list.clear()

        for update in nation.updates:
            self.chinese_updates_list.addItem(update.value)
        for field in nation.fields:
            self.chinese_fields_list.addItem(str(field))

    def updateMongols(self, nation: Nation, points: Points):
        self.mongols_points_label.setText(str(nation.getPoints(points))) 
        self.mongols_age_label.setText(str(nation.age.value))
        self.mongols_villagers_label.setText(str(nation.villagers))
        self.mongols_food_label.setText(str(nation.resources.food))
        self.mongols_wood_label.setText(str(nation.resources.wood))
        self.mongols_stone_label.setText(str(nation.resources.stone))
        self.mongols_gold_label.setText(str(nation.resources.gold))
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

        self.mongols_updates_list.clear()
        self.mongols_fields_list.clear()

        for update in nation.updates:
            self.mongols_updates_list.addItem(update.value)
        for field in nation.fields:
            self.mongols_fields_list.addItem(str(field))
        