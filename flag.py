import math
S = int(input())
print(str(S) + ":")
lstSol = []

for i in range(2,math.ceil(S/2)):
    for j in range(1, math.ceil(S / 2)):
        q = S / (i+j)
        if q != round(q):
            q = (S + j) / (i + j)
            if q != round(q):
                break
        lstSol.append((i, j))
        print((q, i, j))