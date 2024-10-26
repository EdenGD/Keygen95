import random

def generateRetail():
    # Generate first 3 numbers of the product key that are then just runned through a simple blacklist.
    while True:
        a = random.randrange(100, 998)
        if a not in {333, 444, 555, 666, 777, 888}:
            break

    # Generate the last 7 numbers by summing up all digits of b and checking if they're divisible by 7.
    while True:
        b = random.randrange(1000000, 9999997)
        if sum(int(digit) for digit in str(b)) % 7 == 0:
            break
    
    # Put the key together and return.
    return f"{a}-{b}"

def generateOEM():
    # Generate the first 5 digits. They are an ordinal date from 1st january 1995 to 31st december 2003 (although the range in the generator is limited to make it easier)
    a = random.randrange(100, 366)
    b = random.randrange(95, 99)

    # Generates the next 7 digits. It's the same mod7 algorithm from Retail keys except the first digit is always 0 and the last digit cannot equal 0, 8 or 9.
    while True:
        c = random.randrange(100000, 999997)
        c = "0" + str(c)
        if (sum(int(digit) for digit in str(c)) % 7 == 0) and (c[6] not in ["0", "8", "9"]):
            break
    
    # Generate the last 5 characters. Installer doesn't check these using any specific algorithm, they just need to be a number.
    e = random.randrange(10000, 99999)

    # Put the full key together.
    return f"{a}{b}-OEM-{c}-{e}"