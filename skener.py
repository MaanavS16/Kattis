R, C, Zr, Zc = map(int, input().split(" "))
img = []
newImg = []

for i in range(Zr * R):
    layer = []
    for j in range(Zc * C):
        layer.append("")
    newImg.append(layer)

for _ in range(R):
    img.append(list(input()))

for i in range(R):
    for j in range(C):
        for x in range(Zr):
            for y in range(Zc):
                newImg[i*Zr + x][j*Zc + y] = img[i][j]
                #print(i, j, x, y)

for i in newImg:
    strline = ""
    for j in i:
        strline += str(j)
    print(strline)


