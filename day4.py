""" How many #s in given range meet criteria for password?
- never a decrease moving left to right
- at least one instance of a duplicate number, and it only counts if only a duplicate
- 
"""

r = ("168630", "718098")

def test_range(r):
    low = r[0]
    hits = 0
    x = 0
    while x < 5:
        # print(low, x, low[x])
        # check for rule one
        if int(low) > int(r[1]): break
        if int(low[x]) > int(low[x+1]):
            low = str(int(low)+10**(4-x))
            x = 0
            continue
        # check for rule two
        if x == 4:
            L = [int(low[i]) for i in range(len(low))]
            print(L)
            j = []
            k = []
            l = []
            m = []
            n = []
            for i in L:
                if i in j or j == []:
                    j.append(i)
                    continue
                if i in k or k == []:
                    k.append(i)
                    continue
                if i in l or l == []:
                    l.append(i)
                    continue
                if i in m or m == []:
                    m.append(i)
                    continue
                if i in n or n == []:
                    n.append(i)
                    continue
            print(j,k,l,m,n)
            if len(j) == 2 or len(k) == 2 or len(l) == 2 or len(m) == 2 or len(n) == 2:
                print(low)
                hits += 1
                # break
            # for i in range(len(low)-1):
            #     if low[i] == low[i+1] and i < 4 and low[i] != low[i+2] and i > 0 and low[i] != low[i-1]:
            #         print(low)
            #         hits += 1
            #         # low = str(int(low) + 1)
            #         break
            low = str(int(low)+1)
            x = 0
            continue
        x += 1
    print(low)
    return hits

# 690 was too low
print(test_range(r))