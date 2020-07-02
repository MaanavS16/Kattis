N, M = map(int, input().split())

def maxIndex(x):
    y = 0
    for i in x:
        if i > y:
            y = i
    return y

def printVals(x, key, m):
    out = []
    for i in range(len(x)):
        if x[i] == m:
            print(key[i])

listN = []
listM = []

for i in range(N):
    listN.append(i + 1)
for i in range(M):
    listM.append(i + 1)

#print(listN, listM)

listComb = []

for i in listN:
    for j in listM:
        listComb.append(i + j)

lsol = []
lnum = []

for i in listComb:
    if i not in lsol:
        lsol.append(i)
        lnum.append(1)
    else:
        lnum[lsol.index(i)] += 1

printVals(lnum, lsol, maxIndex(lnum))