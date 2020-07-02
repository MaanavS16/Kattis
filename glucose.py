tc = int(input())
points = []
for _ in range(tc):
    points.append(tuple(map(float, input().split(" "))))
trapSum = 0
for i in range(0, len(points) - 1):
    trapSum += (points[i+1][0] - points[i][0])*((points[i+1][1] + points[i][1])/2)
print(trapSum/1000)