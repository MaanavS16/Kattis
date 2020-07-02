def sumnum(n):
    n = str(n)
    sum = 0
    for i in n:
        sum += int(i)
    return sum

while True:
    N = int(input())
    if N == 0:
        break
    sumN = sumnum(N)
    p = 0
    while True:
        Nprime = N * p
        if sumnum(Nprime) == sumN:
            print(p)
            break
        p += 1
