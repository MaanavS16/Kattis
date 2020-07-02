import math
while True:
    n = int(input())
    if n == 0:
        break
    print(math.e**(math.lgamma(n+1) + n + -.5*math.log(2*math.pi) + math.log(n)*(-.5 - n)))
