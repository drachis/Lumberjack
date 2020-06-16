import math
import lumber
import random

@lumber.jack
def pickANumber(a):
    if a:
        return a
    else:
        return random.randint(0,10)

@lumber.jack
def round(a):
    if  (a % 1) > 0.5:
        return math.ceil(a)
    else:
        return math.floor(a)

@lumber.jack
def root(a):
    return math.pow(a,0.5)

if __name__ == "__main__":
    for i in range(1,10):
        round(root(pickANumber(i)))