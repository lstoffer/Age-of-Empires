from typing import List
from typing import Dict
from utils.UpdateType import UpdateType
from utils.AgeType import AgeType
from utils.Ressources import Ressources
from utils.Troops import Troops
from utils.Buildings import Buildings
from utils.BuildingInstances import BuildingInstances
from utils.TroopInstances import TroopInstances
from Villager import Villager
from Update import Update

class Nation:
    def __init__(
        self,
        points: int,
        updates: List[UpdateType],
        age: AgeType,
        fields: List[int],
        ressources: Ressources,
        troops: Troops,
        buildings: Buildings,
        villagers: int,
        buildingInstances: BuildingInstances,
        troopInstances: TroopInstances,
        villagerInstance: Villager,
        updateInstances: Dict[UpdateType, Update]
    ) -> None:
        self.points = points
        self.updates = updates
        self.age = age
        self.fields = fields
        self.ressources = ressources
        self.troops = troops
        self.buildings = buildings
        self.villagers = villagers
        self.buildingInstances = buildingInstances
        self.troopInstances = troopInstances
        self.villagerInstance = villagerInstance
        self.updateInstances = updateInstances

        self.__applyUpdates()

    @classmethod
    def from_dict(cls, nationDict: dict, buildingsDict: dict, troopsDict: dict, villagerDict: dict, updateDict: dict):
        points = nationDict['points']
        updates = [UpdateType(update) for update in nationDict['updates']]
        age = AgeType(nationDict['age'])
        fields = [int(field) for field in nationDict['fields']]
        ressources = Ressources.from_dict(nationDict['ressources'])
        troops = Troops.from_dict(nationDict['troops'])
        buildings = Buildings.from_dict(nationDict['buildings'])
        villagers = nationDict['villagers']

        buildingInstances = BuildingInstances.from_dict(buildingsDict)
        troopInstances = TroopInstances.from_dict(troopsDict)
        villagerInstance = Villager.from_dict(villagerDict)
        updateInstances = {updateType: Update.from_dict(updateDict[updateType]) for updateType in updates}

        return cls(points, updates, age, fields, ressources, 
                   troops, buildings, villagers, buildingInstances, 
                   troopInstances, villagerInstance, updateInstances)
    
    def addUpdate(self, updateType: UpdateType, update: Update):
        self.updates.append(updateType)
        self.updateInstances[updateType] = update
        self.__applyUpdate(update)
    
    def __applyUpdate(self, update: Update):
        self.buildingInstances += update.buildingInstances
        self.troopInstances += update.troopInstances
        self.villagerInstance += update.villagerInstance

    def __applyUpdates(self):
        iterator = iter(self.updateInstances.values())
        accumulatedUpdate = next(iterator)

        for update in iterator:
            accumulatedUpdate += update

        self.buildingInstances += accumulatedUpdate.buildingInstances
        self.troopInstances += accumulatedUpdate.troopInstances
        self.villagerInstance += accumulatedUpdate.villagerInstance
    
    def serialize(self) -> dict:
        nationsData = {}
        nationsData['points'] = self.points
        nationsData['updates'] = [update.value for update in self.updates]
        nationsData['age'] = self.age.value
        nationsData['fields'] = [str(field) for field in self.fields]
        nationsData['ressources'] = self.ressources.serialize()
        nationsData['troops'] = self.troops.serialize()
        nationsData['buildings'] = self.buildings.serialize()
        nationsData['villagers'] = self.villagers
        return nationsData
