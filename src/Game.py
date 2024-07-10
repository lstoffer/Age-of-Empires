from utils.NationType import NationType
from DataAccess import DataAccess
from PyQt5.QtCore import pyqtSlot
from Borders import Borders
from Nation import Nation
from Nations import Nations
from Fields import Fields
from Points import Points
from Ages import Ages
from utils.Ressources import Ressources


class Game:
    def __init__(self) -> None:
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

    @pyqtSlot(int)
    def applyRessourceDividends(self, rounds: int = 1):
        '''adds all ressources earned by all the villagers of a nation to the nation'''
        for field in self.fields.fields.values():
            ressourceType = field.ressource
            villagersAmount = field.villagers
            nationType = field.nation
            nation = self.nations.getNation(nationType)
            amount = villagersAmount * nation.villagerInstance.profit.get(ressourceType)
            amount = amount * rounds
            nation.ressources.add(ressourceType=ressourceType, amount=amount)

    @pyqtSlot(NationType, Ressources)
    def addRessources(self, nationType: NationType, ressources: Ressources):
        nation = self.nations.getNation(nationType)
        nation.addRessources(ressources)


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