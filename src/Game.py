from utils.NationType import NationType
from DataAccess import DataAccess
from Borders import Borders
from Nation import Nation
from Fields import Fields

class Game:
    def __init__(self) -> None:
        self.dataLoader = DataAccess()
        self.__updatesData = self.dataLoader.updates()
        self.__bordersData = Borders(self.dataLoader.borders())
        self.__buildingsData = self.dataLoader.buildings()
        self.__fieldsData = self.dataLoader.fields()
        self.__nationsData = self.dataLoader.nations()
        self.__troopsData = self.dataLoader.troops()
        self.__villagersData = self.dataLoader.villagers()

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
        
        self.fields = Fields(self.__fieldsData)
        self.borders = Borders(self.__bordersData)

        