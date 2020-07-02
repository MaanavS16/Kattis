x = []
for _ in range(10):
    x.append(int(input()) % 42)
    unique = []
for i in x:
    if i not in unique:
        unique.append(i)
print(len(unique))