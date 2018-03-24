# Solution to Q2
import math

# Modelling population growth using equation: P(future) = P(original)*e^(rt)
def population_growth():
    # where p is P(original)
    p = int(input("Population: "))
    growth_factor = float(input("Growth factor: "))
    t = float(input("Hours to achieve growth: "))
    total_t = int(input("Hours population grows: "))
    # p*growth_factor is P(future)
    r = math.log((p*growth_factor)/p)/t

    # prints P(future) where t = hour
    for hour in range(1, total_t + 1):
        print("Hour {}: {}".format(hour, math.floor(p*math.exp(r*hour))))

population_growth()