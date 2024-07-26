# if else
def if_else(value):
    if value == 1:
        return "one"
    elif value == 2:
        return "two"
    elif value == 3:
        return "three"
    else:
        return "Invalid value"

# switch case
def switch_case(value):
    switch = {
        1: "one",
        2: "two",
        3: "three"
    }
    return switch.get(value, "Invalid value")

# ternary?
def ternary(value):
    return "one" if value == 1 else "Invalid value"
