from copy import deepcopy
inp = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,19,9,23,1,23,13,27,1,10,27,31,2,31,13,35,1,10,35,39,2,9,39,43,2,43,9,47,1,6,47,51,1,10,51,55,2,55,13,59,1,59,10,63,2,63,13,67,2,67,9,71,1,6,71,75,2,75,9,79,1,79,5,83,2,83,13,87,1,9,87,91,1,13,91,95,1,2,95,99,1,99,6,0,99,2,14,0,0]

def computer(L, i = 0, noun = 0, verb = 0):
    """ op codes are 1, 2, 99
    """
    L[1] = noun
    L[2] = verb
    if L[i] == 1:
        print(1)
        L[L[i+3]] = L[L[i+1]] + L[L[i+2]]
        return computer(L, i+4, L[1], L[2])
    elif L[i] == 2:
        print(2)
        L[L[i+3]] = L[L[i+1]] * L[L[i+2]]
        return computer(L, i+4, L[1], L[2])
    elif L[i] == 99:
        return L[0]
    else:
        return("Error at index " + str(i) + ", which equals " + str(L[i]) + ".")

def find(L, a=0, b=0):
    goal = 19690720
    solutions = []
    results = []
    while True:
        L2 = deepcopy(L)
        if (result:=computer(L2, noun=a, verb=b)) != goal:
            if a == 94: results.append([a,b,result])
            a += 1
            if a == 100:
                a = 0
                b += 1
                if b == 100:
                    return solutions, results
        else:
            solutions.append(a*100 + b)
            if a < 99: a += 1
            else: b +=1
print(computer(inp, noun=12, verb=2))    
# print(find(inp))