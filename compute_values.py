import math

def add_arithmetic_mean(values, new_value):
    return (values["arithmetic_mean"] * (values["nb_elements"] - 1) + new_value) / values["nb_elements"]

def add_harmonic_mean(values, new_value):
    return (values["nb_elements"]) / (((values["nb_elements"] - 1) / values["harmonic_mean"]) + (1 / new_value))

def add_standard_deviation(values, new_value):
    top_value = (values["nb_elements"] - 1) * (values["standard_deviation"]**2 + (values["arithmetic_mean"] - values["previous_mean"])**2) + ((new_value - values["arithmetic_mean"])**2)
    return math.sqrt(top_value / values["nb_elements"])

def get_root_mean_square(values):
    return math.sqrt(values["arithmetic_mean"]**2 + values["standard_deviation"]**2)

def update_values(values, new_value):
    values["nb_elements"] += 1
    values["arithmetic_mean"] = add_arithmetic_mean(values, new_value)
    values["harmonic_mean"] = add_harmonic_mean(values, new_value)
    values["standard_deviation"] = add_standard_deviation(values, new_value)
    return values