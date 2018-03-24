# Solution to Q1
import math

def sphere_price():
    radius = float(input("Radius: "))
    cost   = float(input("Cost by square meters: "))
    cost   = cost*4*math.pi*radius**2
    print("Price: $", round(cost,2))

sphere_price()