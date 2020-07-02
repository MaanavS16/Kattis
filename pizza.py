def delrepeats(x):
    y = []
    for i in x:
        if i not in y:
            y.append(i)
    return y

def process(x):
    r = x[0]
    r2 = []
    for i in range(1, len(x)):
        x2 = filter(lambda z: z in r, x[i])
        for j in x2:
            r2.append(j)
    r = filter(lambda z: z in r2, r)
    return delrepeats(r)

tc = int(input())
for _ in range(tc):
    arrMasterCombos = []
    pizzas = int(input())
    for _ in range(pizzas):
        arrCombos = []
        name = input()
        arrHaw = list(map(str, input().split(' ')))
        arrEng = list(map(str, input().split(' ')))
        arrHaw = arrHaw[1:]
        arrEng = arrEng[1:]
        for i in range(len(arrHaw)):
            for j in range(len(arrEng)):
                arrCombos.append((arrHaw[i], arrEng[j]))
        arrMasterCombos.append(arrCombos)
    out = process(arrMasterCombos)
    out.sort()
    for i in out:
        print(i)
    print("")