for _ in range(int(input())):
    degree1 = int(input())
    terms1 = list(map(int, input().split()))
    terms1.reverse()
    degree2 = int(input())
    terms2 = list(map(int, input().split()))
    terms2.reverse()
    #print(terms1, terms2)

    newTerms = []
    for i in range(0,(degree1 + degree2) + 1):
        newTerms.append(0)

    for i in range(0,(degree1 + degree2) + 1):
        for j in range(i + 1):
            try:
                #print(i,j)
                newTerms[(i + j)] += terms1[i] * terms2[j]
                if i != j:
                    #print(j,i)
                    newTerms[(i + j)] += terms1[j] * terms2[i]
            except:
                pass
    newTerms.reverse()
    print(degree1 + degree2)
    out = ""
    for i in newTerms:
        out += str(i) + " "
    print(out[:-1])