# Solution to problem 1

#part 1
def half_square(n):
    # iterates backwards from 5
    for i in range(n, 0, -1):
        print("#"*i)

half_square(5)

def sideways_triangle(n):
    for i in range(1, n):
        print("#"*i)

    half_square(n)

sideways_triangle(5)

