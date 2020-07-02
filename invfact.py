import math
inval = math.factorial(int(input()))
def invfact(v):
    c = 0
    c2 = 2
    v0 = [v]
    while(1):
        v0.append(v0[-1]//c2)
        if v0[-1] == 1:
            return(c+2)
            break
        c2 += 1
        c += 1
print(invfact(inval))
