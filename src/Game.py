import random
from utils.NationType import NationType
from DataAccess import DataAccess
from PyQt5.QtCore import pyqtSignal, pyqtSlot, QObject
from Borders import Borders
from Nation import Nation
from Nations import Nations
from Field import Field
from Fields import Fields
from Points import Points
from Ages import Ages
from utils.TroopType import TroopType
from utils.Ressources import Ressources
from utils.BuildingType import BuildingType
from utils.RessourceType import RessourceType
from utils.UpdateType import UpdateType


class Game(QObject):

    updateNation = pyqtSignal(NationType, Nation, Points)
    updateField = pyqtSignal(Field)
    displayError = pyqtSignal(str)
    displayInfo = pyqtSignal(str)

    def __init__(self) -> None:
        super().__init__()
        self.dataAccess = DataAccess()
        self.__updatesData = self.dataAccess.updates()
        self.__bordersData = self.dataAccess.borders()
        self.__buildingsData = self.dataAccess.buildings()
        self.__fieldsData = self.dataAccess.fields()
        self.__nationsData = self.dataAccess.nations()
        self.__troopsData = self.dataAccess.troops()
        self.__villagersData = self.dataAccess.villagers()
        self.__pointsData = self.dataAccess.points()
        self.__agesData = self.dataAccess.ages()

        self.britons = Nation.from_dict(nationDict=self.__nationsData[NationType.BRITONS.value],
                                        buildingsDict=self.__buildingsData[NationType.BRITONS.value],
                                        troopsDict=self.__troopsData[NationType.BRITONS.value],
                                        villagerDict=self.__villagersData[NationType.BRITONS.value],
                                        updateDict=self.__updatesData[NationType.BRITONS.value])

        self.vikings = Nation.from_dict(nationDict=self.__nationsData[NationType.VIKINGS.value],
                                        buildingsDict=self.__buildingsData[NationType.VIKINGS.value],
                                        troopsDict=self.__troopsData[NationType.VIKINGS.value],
                                        villagerDict=self.__villagersData[NationType.VIKINGS.value],
                                        updateDict=self.__updatesData[NationType.VIKINGS.value])

        self.chinese = Nation.from_dict(nationDict=self.__nationsData[NationType.CHINESE.value],
                                        buildingsDict=self.__buildingsData[NationType.CHINESE.value],
                                        troopsDict=self.__troopsData[NationType.CHINESE.value],
                                        villagerDict=self.__villagersData[NationType.CHINESE.value],
                                        updateDict=self.__updatesData[NationType.CHINESE.value])

        self.mongols = Nation.from_dict(nationDict=self.__nationsData[NationType.MONGOLS.value],
                                        buildingsDict=self.__buildingsData[NationType.MONGOLS.value],
                                        troopsDict=self.__troopsData[NationType.MONGOLS.value],
                                        villagerDict=self.__villagersData[NationType.MONGOLS.value],
                                        updateDict=self.__updatesData[NationType.MONGOLS.value])

        self.nations = Nations(self.britons, self.vikings, self.chinese, self.mongols)

        self.fields = Fields(self.__fieldsData)
        self.borders = Borders(self.__bordersData)

        self.points = Points.from_dict(self.__pointsData)

        self.ages = Ages(self.__agesData)

    @pyqtSlot()
    def stopGame(self):
        self.serialize()

    @pyqtSlot(int)
    def applyResourceDividends(self, rounds: int = 1):
        """adds all resources earned by all the villagers of a nation to the nation"""
        for field in self.fields.fields.values():
            resourceType = field.ressource
            villagersAmount = field.villagers
            nationType = field.nation
            if nationType == NationType.NONE:
                continue
            nation = self.nations.getNation(nationType)
            amount = villagersAmount * nation.villagerInstance.profit.get(resourceType)
            amount = amount * rounds
            nation.ressources.add(ressourceType=resourceType, amount=amount)

    @pyqtSlot(NationType, Ressources)
    def addResources(self, nationType: NationType, resources: Ressources):
        nation = self.nations.getNation(nationType)
        nation.addResources(resources)

    @pyqtSlot(NationType, int, int, int)
    def moveVillagers(self, nationType: NationType, amount: int, fromField: int, toField: int):
        fromFieldInstance = self.fields[fromField]
        toFieldInstance = self.fields[toField]
        if fromFieldInstance.getNation() != nationType or toFieldInstance.getNation() not in [nationType, NationType.NONE]:
            self.displayError.emit("Not abel to move villagers from or two enemy fields")
            return
        if fromFieldInstance.getVillager() < amount:
            self.displayError.emit("Not so many villagers on from field")
            return
        # if not self.borders.checkNeighbour(fromFieldInstance, toFieldInstance): TODO
        #     return # TODO: ERROR MESSAGE
        fromFieldInstance.villagers -= amount
        toFieldInstance.villagers += amount
        toFieldInstance.nation = nationType
        
    @pyqtSlot(NationType, int, int)
    def developVillagers(self, nationType: NationType, field: int, amount: int):
        fieldInstance = self.fields[field]
        if fieldInstance.getNation() not in [nationType, NationType.NONE]:
            self.displayError.emit("Not able to develop resources on enemy field")
            return
        nation = self.nations.getNation(nationType)
        costs = nation.villagerInstance.cost
        if not nation.ressources.isSufficient(costs):
            self.displayError.emit("Not enough resources to develop villager")
            return
        if nation.buildings.towncenter < 1:
            self.displayError.emit("Not able to develop villagers without town center")
            return
        fieldInstance.villagers += amount
        fieldInstance.nation = nationType
        nation.villagers += amount
        nation.ressources -= amount*costs
        
    @pyqtSlot(NationType, int, BuildingType)
    def buildBuilding(self, nationType: NationType, field: int, buildingType: BuildingType):
        fieldInstance = self.fields[field]
        if fieldInstance.getNation() not in [nationType, NationType.NONE]:
            self.displayError.emit("Not abel to build building on enemy field")
            return
        nation = self.nations.getNation(nationType)
        costs = nation.buildingInstances.get(buildingType).cost
        if not nation.ressources.isSufficient(costs):
            self.displayError.emit("Not enough resources to build building")
            return
        fieldInstance.buildings.add(buildingType, 1)
        nation.buildings.add(buildingType, 1)
        nation.ressources -= costs
        fieldInstance.nation = nationType

    @pyqtSlot(NationType, int, BuildingType)
    def destroyBuilding(self, nationType: NationType, field: int, buildingType: BuildingType):
        fieldInstance = self.fields[field]
        if fieldInstance.getNation() != nationType:
            self.displayError.emit("Not abel to destroy building on different nation field")
            return
        if fieldInstance.buildings.getBuilding(buildingType) <= 0:
            self.displayError.emit("No building to destroy")
            return
        fieldInstance.buildings.remove(buildingType, 1)

    @pyqtSlot(NationType, int, int)
    def buildWall(self, nationType: NationType, fieldOne: int, fieldTwo: int):
        try:
            self.borders.addWall(nationType, fieldOne, fieldTwo)
        except Exception as e:
            self.displayError.emit(str(e))

    @pyqtSlot(int, int)
    def destroyWall(self, fieldOne: int, fieldTwo: int):
        try:
            self.borders.destroyWall(fieldOne, fieldTwo)
        except Exception as e:
            self.displayError.emit(str(e))

    @pyqtSlot(NationType)
    def updateAge(self, nationType: NationType):
        nation = self.nations.getNation(nationType)
        currentAge = nation.age
        nextAge = self.ages.nextAge(currentAge)
        costs = self.ages.nextAgeCost(nextAge)

        if not nation.ressources.isSufficient(costs):
            self.displayError.emit("Not enough resources to update age")
            return
        # TODO add check for buildings
        
        nation.age = nextAge

    @pyqtSlot(NationType, TroopType, int, int)
    def developTroops(self, nationType: NationType, troopType: TroopType, fieldNumber: int, amount: int):
        fieldInstance = self.fields[fieldNumber]
        if fieldInstance.getNation() not in [nationType, NationType.NONE]:
            self.displayError.emit("Not able to develop troops on enemy field")
            return
        nation = self.nations.getNation(nationType)
        troopInstance = nation.getTroopInstance(troopType)
        costs = troopInstance.cost
        if not nation.ressources.isSufficient(amount * costs):
            self.displayError.emit("Not enough resources to develop troops")
            return
        if nation.buildings.barracks < 0:
            self.displayError.emit("No barracks to develop troops")
            return
        
        if troopType == TroopType.ARCHER:
            nation.troops.archer += amount
            fieldInstance.troops.archer += amount
        elif troopType == TroopType.INFANTRY:
            nation.troops.infantry += amount
            fieldInstance.troops.infantry += amount
        elif troopType == TroopType.CAVALRY:
            nation.troops.cavalry += amount
            fieldInstance.troops.cavalry += amount
        elif troopType == TroopType.SIEGE:
            nation.troops.siege += amount
            fieldInstance.troops.siege += amount

        nation.ressources -= amount*costs
        fieldInstance.nation = nationType

    @pyqtSlot(NationType, int, int, int, int, int, int)
    def moveTroops(self, nationType: NationType, archerAmount: int, infantryAmount: int, cavalryAmount: int, siegeAmount: int, fromField: int, toField: int):
        fromFieldInstance = self.fields[fromField]
        toFieldInstance = self.fields[toField]
        if fromFieldInstance.getNation() != nationType or toFieldInstance.getNation() not in [nationType, NationType.NONE]:
            self.displayError.emit("Not able to move troops from or two enemy fields")
            return
        if fromFieldInstance.troops.archer < archerAmount:
            self.displayError.emit("Not so many archers on from field")
            return
        elif fromFieldInstance.troops.infantry < infantryAmount:
            self.displayError.emit("Not so many infantry on from field")
            return
        elif fromFieldInstance.troops.cavalry < cavalryAmount:
            self.displayError.emit("Not so many cavalry on from field")
            return
        elif fromFieldInstance.troops.siege < siegeAmount:
            self.displayError.emit("Not so many siege on from field")
            return
        # if not self.borders.checkNeighbour(fromFieldInstance, toFieldInstance): TODO
        #     return # TODO: ERROR MESSAGE
        fromFieldInstance.troops.archer -= archerAmount
        fromFieldInstance.troops.infantry -= infantryAmount
        fromFieldInstance.troops.cavalry -= cavalryAmount
        fromFieldInstance.troops.siege -= siegeAmount
        toFieldInstance.troops.archer += archerAmount
        toFieldInstance.troops.infantry += infantryAmount
        toFieldInstance.troops.cavalry += cavalryAmount
        toFieldInstance.troops.siege += siegeAmount
        toFieldInstance.nation = nationType

    @pyqtSlot(int, int)
    def attack(self, fromField: int, toField: int):
        fromFieldInstance = self.fields[fromField]
        toFieldInstance = self.fields[toField]
        attackNation = self.nations.getNation(fromFieldInstance.nation)
        defenceNation = self.nations.getNation(toFieldInstance.nation)
        
        attackValue = fromFieldInstance.troops.archer * attackNation.troopInstances.archer.attack
        attackValue += fromFieldInstance.troops.cavalry * attackNation.troopInstances.cavalry.attack
        attackValue += fromFieldInstance.troops.infantry * attackNation.troopInstances.infantry.attack
        
        defenceValue = toFieldInstance.troops.archer * defenceNation.troopInstances.archer.defence
        defenceValue += toFieldInstance.troops.cavalry * defenceNation.troopInstances.cavalry.defence
        defenceValue += toFieldInstance.troops.infantry * defenceNation.troopInstances.infantry.defence

        successProb = attackValue / (attackValue + defenceValue)
        success = random.random() < successProb

        if success:
            archerLoss = 10 if toFieldInstance.troops.archer >= 10 else toFieldInstance.troops.archer
            toFieldInstance.troops.archer -= archerLoss
            infantryLoss = 10 if toFieldInstance.troops.infantry >= 10 else toFieldInstance.troops.infantry
            toFieldInstance.troops.infantry -= infantryLoss
            cavalryLoss = 10 if toFieldInstance.troops.cavalry >= 10 else toFieldInstance.troops.cavalry
            toFieldInstance.troops.cavalry -= cavalryLoss
            defenceNation.troops.archer -= archerLoss
            defenceNation.troops.infantry -= infantryLoss
            defenceNation.troops.cavalry -= cavalryLoss
            self.displayInfo.emit(f'Defender lost {archerLoss} archers, {infantryLoss} infantry and {cavalryLoss} cavalry')
        else:
            archerLoss = 10 if fromFieldInstance.troops.archer >= 10 else fromFieldInstance.troops.archer
            fromFieldInstance.troops.archer -= archerLoss
            infantryLoss = 10 if fromFieldInstance.troops.infantry >= 10 else fromFieldInstance.troops.infantry
            fromFieldInstance.troops.infantry -= infantryLoss
            cavalryLoss = 10 if fromFieldInstance.troops.cavalry >= 10 else fromFieldInstance.troops.cavalry
            fromFieldInstance.troops.cavalry -= cavalryLoss
            attackNation.troops.archer -= archerLoss
            attackNation.troops.infantry -= infantryLoss
            attackNation.troops.cavalry -= cavalryLoss
            self.displayInfo.emit(f'Attacker lost {archerLoss} archers, {infantryLoss} infantry and {cavalryLoss} cavalry')

        if toFieldInstance.troops.archer == 0 and toFieldInstance.troops.infantry == 0 and toFieldInstance.troops.cavalry == 0:
            defenceNation.troops.siege -= toFieldInstance.troops.siege
            toFieldInstance.troops.siege = 0

            defenceNation.villagers -= toFieldInstance.villagers
            toFieldInstance.villagers = 0

            structure = toFieldInstance.buildings.towncenter * defenceNation.buildingInstances.towncenter.structure
            structure += toFieldInstance.buildings.castle * defenceNation.buildingInstances.castle.structure

            destruction = fromFieldInstance.troops.siege * attackNation.troopInstances.siege.attack

            if structure <= destruction:
                defenceNation.buildings.towncenter -= toFieldInstance.buildings.towncenter
                defenceNation.buildings.castle -= toFieldInstance.buildings.castle
                toFieldInstance.buildings.towncenter = 0
                toFieldInstance.buildings.castle = 0
                self.displayInfo.emit('All buildings destroyed')

                toFieldInstance.nation = NationType.NONE
            else:
                self.displayInfo.emit(f'Not able to destroy buildings: destruction was {destruction} and structure was {structure}')

        if fromFieldInstance.troops.infantry == 0 and fromFieldInstance.troops.cavalry == 0 and fromFieldInstance.troops.archer == 0 and fromFieldInstance.buildings.towncenter == 0 and fromFieldInstance.buildings.castle == 0:
            fromFieldInstance.nation = NationType.NONE

    @pyqtSlot(NationType, RessourceType, RessourceType, int, int)
    def trade(self, nationType: NationType, fromResourceType: RessourceType, toResourceType: RessourceType, fromAmount: int, toAmount: int):
        nation = self.nations.getNation(nationType)
        available = nation.ressources.get(fromResourceType)
        if available < fromAmount:
            self.displayError.emit("Not enough resources")
            return
        nation.ressources.add(toResourceType, toAmount)
        nation.ressources.add(fromResourceType, -fromAmount)

    @pyqtSlot(NationType, UpdateType)
    def applyUpdate(self, nationType: NationType, updateType: UpdateType):
        nation = self.nations.getNation(nationType)
        try:
            nation.addUpdate(updateType)
        except Exception as e:
            self.displayError.emit(str(e))

    @pyqtSlot(int)
    def updateFields(self, fieldNumber: int):
        if fieldNumber in self.fields.fieldNumbers():
            field = self.fields[fieldNumber]
            self.updateField.emit(field)

    @pyqtSlot()
    def updateNations(self):
        self.updateNation.emit(NationType.BRITONS, self.nations.britons, self.points)
        self.updateNation.emit(NationType.VIKINGS, self.nations.vikings, self.points)
        self.updateNation.emit(NationType.CHINESE, self.nations.chinese, self.points)
        self.updateNation.emit(NationType.MONGOLS, self.nations.mongols, self.points)

    def serialize(self):
        bordersData = self.borders.serialize()
        fieldsData = self.fields.serialize()
        nationsData = self.nations.serialize()
        pointsData = self.points.serialize()

        self.dataAccess.storeData('borders_data.json', bordersData)
        self.dataAccess.storeData('fields_data.json', fieldsData)
        self.dataAccess.storeData('nations_data.json', nationsData)
        self.dataAccess.storeData('points_data.json', pointsData)


game = Game()
