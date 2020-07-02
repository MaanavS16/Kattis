for _ in range(int(input())):
    lstVals = list(map(int, input().split(" ")))
    lstVals.remove(0)
    sum = 0
    for i in lstVals:
        try:
            if lstVals[lstVals.index(i) + 1] > 2*i:
                sum += lstVals[lstVals.index(i) + 1] - 2*i
        except:
            sum += 0
    print(sum)