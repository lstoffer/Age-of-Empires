from enum import Enum


class TroopType(Enum):
    CAVALRY = "cavalry"
    INFANTRY = "infantry"
    ARCHER = "archer"
    SIEGE = "siege"


# Assuming you have the string "cavalry"
troop_type_str = "cavalry"

# Get the corresponding enum member
troop_type_enum = TroopType(troop_type_str)

print(troop_type_enum) 