import sys
import math
for line in sys.stdin:
    n = int(line)
    if n == 0 or n == 1:
        print(1)
    else:
        print(math.floor(.5*math.log10(2*n*(math.pi)) + n*(math.log10(n/(math.e)))) +1)
