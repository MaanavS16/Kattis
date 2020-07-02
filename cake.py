n,h,v = input().split()
n = int(n)
h = int(h)
v = int(v)
if (n-h) > h:
    h = n-h
if (n-v) > v:
    v = n-v
print(4*v*h)
