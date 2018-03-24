# Solution to Q4

# finds the greatest common divisor of two positive integers using Euclid's algorithm
def gcd():
    a = int(input("a: "))
    b = int(input("b: "))
    # input validation
    while a < 1 or b < 1:
        print("Error. Enter positive integers for a and b")
        a = int(input("a: "))
        b = int(input("b: "))
    # rearranging the values so that a is always greater than or equal to b
    if b > a:
        a, b = b, a
    
    while b != 0:
        a, b = b, a % b
        print("a: {}, b: {}".format(a, b))
    
    print("GCD:", a)

gcd()