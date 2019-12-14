from day5 import computer
from copy import deepcopy

inp = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
phases = [4, 3, 2, 1, 0]

def thrust(L, poss):
    """ Iterates through a possibility.
    """
    print("first")
    x = deepcopy(L)
    z = computer(x, I1 = poss[0], I2 = 0)
    # O = computer(x)
    print("second")
    x = deepcopy(L)
    z = computer(x, I1 = poss[1], I2 = z)
    # O = computer(x)
    print("third")
    x = deepcopy(L)
    z = computer(x, I1 = poss[2], I2 = z)
    # O = computer(x)
    print("fourth")
    x = deepcopy(L)
    z = computer(x, I1 = poss[3], I2 = z)
    # O = computer(x)
    print("fifth")
    x = deepcopy(L)
    return computer(x, I1 = poss[4], I2 = z)
    # return computer(x)

def iterations(L, P):
    """ Goes through all iterations.
    """
    return
    
print(thrust(inp, phases))