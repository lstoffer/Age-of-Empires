from utils.NationType import NationType

# Original dictionary
original_dict = {
    "111": {"111": "", "112": "mongols", "113": "mongols", "114": "britons"},
    "112": {"111": "mongols", "112": "britons", "113": "mongols", "114": "mongols"},
    "113": {"111": "mongols", "112": "mongols", "113": "britons", "114": "mongols"},
    "114": {"111": "britons", "112": "mongols", "113": "mongols", "114": "britons"}
}

# Using nested dictionary comprehension to manipulate the values
manipulated_dict = {
    int(outer_key): {int(inner_key): (NationType(value) if value != "" else None) for inner_key, value in outer_value.items()}
    for outer_key, outer_value in original_dict.items()
}

# Printing the manipulated dictionary
print(manipulated_dict)


print(manipulated_dict[111][112])