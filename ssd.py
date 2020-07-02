import math

for _ in range(int(input())):
    sum = 0
    K, B, N = map(int, input().split())
    #print(K, B, N)
    if N == 1:
        print(str(K), "1")
    else:
        p = 0
        while B**p < N:
            p += 1
        for i in range(p):
            q = p - i - 1
            bn = math.floor(N / B**q)
            N -= (B**q) * bn
            sum += bn**2
        print(str(K), str(su*m))