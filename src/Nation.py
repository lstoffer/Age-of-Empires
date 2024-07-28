from typing import List
from utils.TroopType import TroopType
from utils.UpdateType import UpdateType
from utils.AgeType import AgeType
from utils.Ressources import Ressources
from utils.Troops import Troops
from utils.Buildings import Buildings
from utils.BuildingInstances import BuildingInstances
from utils.TroopInstances import TroopInstances
from Villager import Villager
from Update import Update
from Points import Points
from Troop import Troop
from Updates import Updates


class Nation:
    def __init__(
        self,
        points: int,
        updates: List[UpdateType],
        age: AgeType,
        fields: List[int],
        resources: Ressources,
        troops: Troops,
        buildings: Buildings,
        villagers: int,
        buildingInstances: BuildingInstances,
        troopInstances: TroopInstances,
        villagerInstance: Villager,
        updateInstances: Updates
    ) -> None:
        self.__points = points      # Only used to store the points after playing not to access the points during play
        self.updates = updates
        self.age = age
        self.fields = fields
        self.resources = resources
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
        resources = Ressources.from_dict(nationDict['resources'])
        troops = Troops.from_dict(nationDict['troops'])
        buildings = Buildings.from_dict(nationDict['buildings'])
        villagers = nationDict['villagers']

        buildingInstances = BuildingInstances.from_dict(buildingsDict)
        troopInstances = TroopInstances.from_dict(troopsDict)
        villagerInstance = Villager.from_dict(villagerDict)
        updateInstances = Updates(updateDict)

        return cls(points, updates, age, fields, resources,
                   troops, buildings, villagers, buildingInstances, 
                   troopInstances, villagerInstance, updateInstances)
    
    def addResources(self, resources: Ressources):
        self.resources += resources
    
    def addUpdate(self, updateType: UpdateType):
        update = self.updateInstances.getUpdate(updateType)
        costs = update.cost

        if not self.resources.isSufficient(costs):
            raise Exception("Not enough resources to add update")

        self.buildingInstances += update.buildingInstances
        self.troopInstances += update.troopInstances
        self.villagerInstance += update.villagerInstance

        self.resources -= costs

        self.updates.append(updateType)

    def getAttack(self, troops: Troops) -> int:
        archerAttack = troops.archer * self.troopInstances.archer.attack
        infantryAttack = troops.infantry * self.troopInstances.infantry.attack
        cavalryAttack = troops.cavalry * self.troopInstances.cavalry.attack
        return archerAttack + infantryAttack + cavalryAttack

    def getSiegeAttack(self, troops: Troops) -> int:
        return troops.siege * self.troopInstances.siege.attack
    
    def getDefence(self, troops: Troops) -> int:
        archerDef = troops.archer * self.troopInstances.archer.defence
        infantryDef = troops.infantry * self.troopInstances.infantry.defence
        cavalryDef = troops.cavalry * self.troopInstances.cavalry.defence
        return archerDef + infantryDef + cavalryDef

    def getTroopInstance(self, troopType: TroopType) -> Troop:
        if troopType == TroopType.ARCHER:
            return self.troopInstances.archer
        elif troopType == TroopType.INFANTRY:
            return self.troopInstances.infantry
        elif troopType == TroopType.CAVALRY:
            return self.troopInstances.cavalry
        elif troopType == TroopType.SIEGE:
            return self.troopInstances.siege
    
    def getPoints(self, points: Points) -> int:
        nationPoints = 0
        # Age Points
        nationPoints += points.ages[self.age]
        # Troop Points
        nationPoints += self.troops.archer * self.troopInstances.archer.points
        nationPoints += self.troops.infantry * self.troopInstances.infantry.points
        nationPoints += self.troops.cavalry * self.troopInstances.cavalry.points
        nationPoints += self.troops.siege * self.troopInstances.siege.points
        nationPoints += self.villagers * self.villagerInstance.points
        # Building Points
        nationPoints += self.buildings.towncenter * self.buildingInstances.towncenter.points
        nationPoints += self.buildings.market * self.buildingInstances.market.points
        nationPoints += self.buildings.barracks * self.buildingInstances.barracks.points
        nationPoints += self.buildings.wall * self.buildingInstances.wall.points
        nationPoints += self.buildings.castle * self.buildingInstances.castle.points
        nationPoints += self.buildings.university * self.buildingInstances.university.points
        self.__points = nationPoints
        return nationPoints

    def __applyUpdates(self):
        if not self.updates:
            return

        accumulatedUpdate = self.updateInstances.getUpdate(self.updates.pop(0))
        for update in self.updates:
            accumulatedUpdate += self.updateInstances.getUpdate(update)

        self.buildingInstances += accumulatedUpdate.buildingInstances
        self.troopInstances += accumulatedUpdate.troopInstances
        self.villagerInstance += accumulatedUpdate.villagerInstance

    def serialize(self) -> dict:
        nationsData = {
           'points': self.__points,
           'updates': [update.value for update in self.updates],
           'age': self.age.value,
           'fields': [str(field) for field in self.fields],
           'resources': self.resources.serialize(),
           'troops': self.troops.serialize(),
           'buildings': self.buildings.serialize(),
           'villagers': self.villagers
        }
        return nationsData
