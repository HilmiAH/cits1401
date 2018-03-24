# Solution to Q3
import math

# Using equation for compound interest: A = P(1 + r/n)^(nt)
def years_to_double():
    r = float(input("Interest rate: "))
    n = float(input("# of times compounded in a year: "))
    t = math.log(2)/math.log(1 + r / 100 / n) / n
    print("It takes {} year(s) to double your money at {}% compounded {} time(s) a year.".format(round(t,2), r, n))

years_to_double()