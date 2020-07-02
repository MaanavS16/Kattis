import math

n = (int(input()) + 1)
if n < 50:
    n1 = 0
    for i in range(1,n):
        n1 += ((-1)**i) / math.factorial(i)

    print(-n1)
else:
    print(1 - 0.367879441171442)