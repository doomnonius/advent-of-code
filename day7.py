from day5 import computer

inp = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]

def thrusters(L):
    phases = [0, 1, 2, 3, 4]
    out = None
    
    computer(inp, I1 = phases[0], I2 = 0)