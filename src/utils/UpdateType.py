from enum import Enum


class UpdateType(Enum):
    WHEEL = 'wheel'
    TRADE_CART = 'trade-cart'
    SHORT_SWORDSMAN = 'short-swordsman'
    LONG_SWORDSMAN = 'long-swordsman'
    HEAVY_CAVALRY = 'heavy-cavalry'
    WAR_ELEPHANT = 'war-elephant'
    IMPROVED_BOWMAN = 'improved-bowman'
    COMPOSITE_BOWMAN = 'composite-bowman'
    CENTURION = 'centurion'
    LEGIONARY = 'legionary'
    STONE_THROWER = 'stone-thrower'
    TREBUCHET = 'trebuchet'
    GOLD_MINING = 'gold-mining'
    GOLD_MINING_II = 'gold-mining-ii'
    STONE_MINING = 'stone-mining'
    STONE_MINING_II = 'stone-mining-ii'
    WOODCUTTING = 'woodcutting'
    ARTISANSHIP = 'artisanship'
    DOMESTICATION = 'domestication'
    PLOW = 'plow'
    BIG_WALL = 'big-wall'
    STONE_WALL = 'stone-wall'
    BIG_CASTLE = 'big-castle'
    STONE_CASTLE = 'stone-castle'

class UpdateCategory(Enum):
    BUILDINGS = 'buildings'
    TROOPS = 'troops'
    VILLAGERS = 'villagers'
    COSTS = 'costs'
    