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


class Game(QObject):

    updateNation = pyqtSignal(NationType, Nation)
    updateField = pyqtSignal(Field)
    displayError = pyqtSignal(str)

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
    def applyRessourceDividends(self, rounds: int = 1):
        '''adds all ressources earned by all the villagers of a nation to the nation'''
        for field in self.fields.fields.values():
            ressourceType = field.ressource
            villagersAmount = field.villagers
            nationType = field.nation
            if nationType == NationType.NONE:
                continue
            nation = self.nations.getNation(nationType)
            amount = villagersAmount * nation.villagerInstance.profit.get(ressourceType)
            amount = amount * rounds
            nation.ressources.add(ressourceType=ressourceType, amount=amount)

    @pyqtSlot(NationType, Ressources)
    def addRessources(self, nationType: NationType, ressources: Ressources):
        nation = self.nations.getNation(nationType)
        nation.addRessources(ressources)

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
        # if fieldInstance.buildings.towncenter <= 0:
        #     return # TODO: ERROR MESSAGE
        if fieldInstance.getNation() not in [nationType, NationType.NONE]:
            self.displayError.emit("Not able to develop ressources on enemy field")
            return
        nation = self.nations.getNation(nationType)
        costs = nation.villagerInstance.cost
        if not nation.ressources.isSufficient(costs):
            self.displayError.emit("Not enough ressources to develop villager")
            return
        if nation.buildings.towncenter < 1:
            self.displayError.emit("Not able to develop villagers without towncenter")
            return
        fieldInstance.villagers += amount
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
            self.displayError.emit("Not enough ressources to build building")
            return
        fieldInstance.buildings.add(buildingType, 1)
        nation.buildings.add(buildingType, 1)
        nation.ressources -= costs

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

    @pyqtSlot(NationType)
    def updateAge(self, nationType: NationType):
        nation = self.nations.getNation(nationType)
        currentAge = nation.age
        nextAge = self.ages.nextAge(currentAge)
        costs = self.ages.nextAgeCost(nextAge)

        if not nation.ressources.isSufficient(costs):
            self.displayError.emit("Not enough ressources to update age")
            return
        # TODO add check for buildings
        
        nation.age = nextAge

    @pyqtSlot(NationType, TroopType, int, int)
    def developTroops(self, nationType: NationType, troopType: TroopType, fieldNumber: int, amount: int):
        fieldInstance = self.fields[fieldNumber]
        # if fieldInstance.buildings.towncenter <= 0:
        #     return # TODO: ERROR MESSAGE
        if fieldInstance.getNation() not in [nationType, NationType.NONE]:
            self.displayError.emit("Not able to develop troops on enemy field")
            return
        nation = self.nations.getNation(nationType)
        troopInstance = nation.getTroopInstance(troopType)
        costs = troopInstance.cost
        if not nation.ressources.isSufficient(amount * costs):
            self.displayError.emit("Not enough ressources to develop troops")
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
            self.displayError.emit(f'Defender lost {archerLoss} archers, {infantryLoss} infantry and {cavalryLoss} cavalry')
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
            self.displayError.emit(f'Attacker lost {archerLoss} archers, {infantryLoss} infantry and {cavalryLoss} cavalry')

        if toFieldInstance.troops.archer == 0 and toFieldInstance.troops.infantry == 0 and toFieldInstance.troops.cavalry == 0:
            defenceNation.troops.siege -= toFieldInstance.troops.siege
            toFieldInstance.troops.siege = 0

            structure = toFieldInstance.buildings.towncenter * defenceNation.buildingInstances.towncenter.structure
            structure += toFieldInstance.buildings.castle * defenceNation.buildingInstances.castle.structure

            destruction = fromFieldInstance.troops.siege * attackNation.troopInstances.siege.attack

            if structure <= destruction:
                defenceNation.buildings.towncenter -= toFieldInstance.buildings.towncenter
                defenceNation.buildings.castle -= toFieldInstance.buildings.castle
                toFieldInstance.buildings.towncenter = 0
                toFieldInstance.buildings.castle = 0
                self.displayError.emit('All buildings destroyed')

                toFieldInstance.nation = NationType.NONE
            else:
                self.displayError.emit(f'Not able to destroy buildings: destruction was {destruction} and structure was {structure}')

        # TODO: Felder zurückgeben
        if fromFieldInstance.troops.infantry == 0 and fromFieldInstance.troops.cavalry == 0 and fromFieldInstance.troops.archer == 0 and fromFieldInstance.buildings.towncenter == 0 and fromFieldInstance.castle == 0:
            fromFieldInstance.nation = NationType.NONE

        

    @pyqtSlot(NationType, RessourceType, RessourceType, int, int)
    def trade(self, nationType: NationType, fromRessourceType: RessourceType, toRessourceType: RessourceType, fromAmount: int, toAmount: int):
        nation = self.nations.getNation(nationType)
        available = nation.ressources.get(fromRessourceType)
        if available < fromAmount:
            self.displayError.emit("Not enough ressources")
            return
        nation.ressources.add(toRessourceType, toAmount)
        nation.ressources.add(fromRessourceType, -fromAmount)

    @pyqtSlot(int)
    def updateFields(self, fieldNumber: int):
        if fieldNumber in self.fields.fieldNumbers():
            field = self.fields[fieldNumber]
            self.updateField.emit(field)

    @pyqtSlot()
    def updateNations(self):
        self.updateNation.emit(NationType.BRITONS, self.nations.britons)
        self.updateNation.emit(NationType.VIKINGS, self.nations.vikings)
        self.updateNation.emit(NationType.CHINESE, self.nations.chinese)
        self.updateNation.emit(NationType.MONGOLS, self.nations.mongols)

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
print('here')