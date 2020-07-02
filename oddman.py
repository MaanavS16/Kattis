for r in range(int(input())):
    theif = None
    people = int(input())
    lstC = list(map(int, input().split(" ")))
    for i in lstC:
        temp = lstC.copy()
        temp.remove(i)
        if i not in temp:
            print("Case #" + str(r+1)+": " + str(i))
            break