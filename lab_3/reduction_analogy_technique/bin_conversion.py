# Solution to Q5

# Converts a binary string to a decimal integer
def bin_to_dec(b):
    dec = 0

    # b[::-1] reverses the string (using extended slice).
    # i is the index of the bit in the string, which we use to calculate the value in decimal if it is a 1
    # then add it to dec
    for i, c in enumerate(b[::-1]):
        if c == "1":
            dec += 2**i
    
    return dec

def dec_to_bin(d):
    bin = ""
    # conversion using the "repeated division by 2" method
    while d != 0:
        d, bit = divmod(d, 2)
        bin += str(bit)

    # add extra 0's if necessary
    bin += "0"*(8 - len(bin))
    # reverses the string to return a proper binary
    return bin[::-1]