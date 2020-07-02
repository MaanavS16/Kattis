import math
arrNums = [0,1,2,3,4,5,6]
arrDays = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday" ]
j = 20
q,m = input().split(" ")
q = int(q)
m = int(m)
if m == 1 or m == 2:
    m = 12 + m
    k = 8
else:
    k = 9
h = (q + math.floor(13*(m+1)/5) + k + math.floor(k/4) + math.floor(j/4) - 2*j) % 7
print(arrDays[arrNums.index(h)])
