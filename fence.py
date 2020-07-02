import math
A, N = map(float, input().split(" "))
r = N / (math.pi * 2)
Area = math.pi * r**2
if (Area) >= A:
    print("Diablo is happy!")
else:
    print("Need more materials!")