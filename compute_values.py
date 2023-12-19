import math

def add_arithmetic_mean(values, new_value):
    if (new_value == 0):
        print("104neutrinos: Value must not be equal to 0")
        exit(84)
    try:
        return (values["arithmetic_mean"] * (values["nb_elements"] - 1) + new_value) / values["nb_elements"]
    except:
        print("104neutrinos: Cannot add value, implies division by zero")
        exit(84)

def add_harmonic_mean(values, new_value):
    if (new_value == 0):
        print("104neutrinos: Value must not be equal to 0")
        exit(84)
    try:
        return (values["nb_elements"]) / (((values["nb_elements"] - 1) / values["harmonic_mean"]) + (1 / new_value))
    except:
        print("104neutrinos: Cannot add value, implies division by zero")
        exit(84)

def add_standard_deviation(values, new_value):
    if (new_value == 0):
        print("104neutrinos: Value must not be equal to 0")
        exit(84)
    top_value = (values["nb_elements"] - 1) * (values["standard_deviation"]**2 + (values["arithmetic_mean"] - values["previous_mean"])**2) + ((new_value - values["arithmetic_mean"])**2)
    try:
        return math.sqrt(top_value / values["nb_elements"])
    except:
        print("104neutrinos: Cannot add value, implies division by zero")
        exit(84)

def get_root_mean_square(values):
    return math.sqrt(values["arithmetic_mean"]**2 + values["standard_deviation"]**2)

def update_values(values, new_value):
    values["nb_elements"] += 1
    values["arithmetic_mean"] = add_arithmetic_mean(values, new_value)
    values["harmonic_mean"] = add_harmonic_mean(values, new_value)
    values["standard_deviation"] = add_standard_deviation(values, new_value)
    return values