while True:
    n = int(input())
    if n == 0:
        break
    else:
        list1 = []
        list2 = []
        for _ in range(n):
            list1.append(int(input()))
        for _ in range(n):
            list2.append(int(input()))
        slist1 = sorted(list1)
        slist2 = sorted(list2)
        flist = []
        for i in range(len(slist1)):
            index = slist1.index(list1[i])
            flist.append(slist2[index])
        for i in range(len(flist) + 1):
            try:
                print(flist[i])
            except:
                print()