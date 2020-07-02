run = 0
while(True):
    inval = int(input())
    if inval == 0:
        break
    run += 1
    print("SET", str(run))

    if inval % 2 == 1:
        forward = round(inval/2 + .5)
    else:
        forward = inval/2

    reverse = inval - forward

    lstStrings = []
    for _ in range(inval):
        lstStrings.append(str(input()))

    for i in range(int(forward)):
        print(lstStrings[2*i])
    for i in range(int(reverse)):
        print(lstStrings[int(reverse - i) * 2 - 1])
