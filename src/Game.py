from utils.NationType import NationType
from DataAccess import DataAccess
from Borders import Borders
from Nation import Nation
from Nations import Nations
from Fields import Fields
from Points import Points
from Ages import Ages


class Game:
    def __init__(self) -> None:
        self.dataAccess = DataAccess()
        self.__updatesData = self.dataAccess.updates()
        # self.__bordersData = Borders(self.dataAccess.borders())
        self.__buildingsData = self.dataAccess.buildings()
        # self.__fieldsData = self.dataAccess.fields()
        # self.__nationsData = self.dataAccess.nations()
        self.__troopsData = self.dataAccess.troops()
        self.__villagersData = self.dataAccess.villagers()
        # self.__pointsData = self.dataAccess.points()
        self.__agesData = self.dataAccess.ages()

        self.britons = Nation.from_dict(nationDict=self.__nationsData[NationType.BRITONS],
                                        buildingsDict=self.__buildingsData[NationType.BRITONS],
                                        troopsDict=self.__troopsData[NationType.BRITONS],
                                        villagerDict=self.__villagersData[NationType.BRITONS],
                                        updateDict=self.__updatesData[NationType.BRITONS])

        self.vikings = Nation.from_dict(nationDict=self.__nationsData[NationType.VIKINGS],
                                        buildingsDict=self.__buildingsData[NationType.VIKINGS],
                                        troopsDict=self.__troopsData[NationType.VIKINGS],
                                        villagerDict=self.__villagersData[NationType.VIKINGS],
                                        updateDict=self.__updatesData[NationType.VIKINGS])

        self.chinese = Nation.from_dict(nationDict=self.__nationsData[NationType.CHINESE],
                                        buildingsDict=self.__buildingsData[NationType.CHINESE],
                                        troopsDict=self.__troopsData[NationType.CHINESE],
                                        villagerDict=self.__villagersData[NationType.CHINESE],
                                        updateDict=self.__updatesData[NationType.CHINESE])

        self.mongols = Nation.from_dict(nationDict=self.__nationsData[NationType.MONGOLS],
                                        buildingsDict=self.__buildingsData[NationType.MONGOLS],
                                        troopsDict=self.__troopsData[NationType.MONGOLS],
                                        villagerDict=self.__villagersData[NationType.MONGOLS],
                                        updateDict=self.__updatesData[NationType.MONGOLS])

        self.nations = Nations(self.britons, self.vikings, self.chinese, self.mongols)

        self.fields = Fields(self.__fieldsData)
        self.borders = Borders(self.__bordersData)

        self.points = Points(self.__pointsData)

        self.ages = Ages(self.__agesData)

    def serialize(self):
        bordersData = self.borders.serialize()
        fieldsData = self.fields.serialize()
        nationsData = self.nations.serialize()
        pointsData = self.points.serialize()

        self.dataAccess.storeData('borders_data.json', bordersData)
        self.dataAccess.storeData('fields_data.json', fieldsData)
        self.dataAccess.storeData('nations_data.json', nationsData)
        self.dataAccess.storeData('points_data.json', pointsData)
