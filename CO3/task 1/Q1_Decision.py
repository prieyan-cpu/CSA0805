households = [
    (100, False, False),
    (101, True, False),
    (150, False, False),
    (200, True, False),
    (201, False, False),
    (250, False, True),
    (80, True, True),
    (180, True, True)
]


def separate_if(units, ration, elderly):
    result = []

    if units <= 100:
        result.append("Full Subsidy")

    if units <= 200 and ration:
        result.append("Partial Subsidy")

    if units > 200 and elderly:
        result.append("Elderly Subsidy")

    if len(result) == 0:
        result.append("No Subsidy")

    return result


def elif_decision(units, ration, elderly):
    if units <= 100:
        return "Full Subsidy"

    elif 101 <= units <= 200:
        if ration:
            return "Partial Subsidy"
        else:
            return "No Subsidy"

    elif units > 200:
        if elderly:
            return "Elderly Subsidy"
        else:
            return "No Subsidy"


print("HOUSEHOLD SUBSIDY RESULTS")

for i, (units, ration, elderly) in enumerate(households, 1):
    print("\nHousehold", i)
    print("Units:", units)
    print("Ration Card:", ration)
    print("Elderly Member:", elderly)
    print("Separate if:", separate_if(units, ration, elderly))
    print("If-elif-else:", elif_decision(units, ration, elderly))