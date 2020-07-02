def calcAvg(x):
    sum = 0
    for i in x:
        sum += i
    return(sum / len(x))


for _ in range(int(input())):
    grade = list(map(int, input().split()))[1:]
    avg = calcAvg(grade)
    count = 0
    for i in grade:
        if i > avg:
            count += 1
    print(str(format(round(100 * count/len(grade), 3), '.3f')) + "%")

