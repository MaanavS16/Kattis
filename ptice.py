charLen = int(input())
answer = list(input())

Adrian = []
Bruno = []
Goran = []

for i in range(1,charLen + 1):
    if i % 3 == 1:
        Adrian.append("A")
    elif i % 3 == 2:
        Adrian.append("B")
    elif i % 3 == 0:
        Adrian.append("C")

    if i % 4 == 1:
        Bruno.append("B")
    elif i % 4 == 2:
        Bruno.append("A")
    elif i % 4 == 3:
        Bruno.append("B")
    elif i % 4 == 0:
        Bruno.append("C")

    if i % 6 == 1:
        Goran.append("C")
    elif i % 6 == 2:
        Goran.append("C")
    elif i % 6 == 3:
        Goran.append("A")
    elif i % 6 == 4:
        Goran.append("A")
    elif i % 6 == 5:
        Goran.append("B")
    elif i % 6 == 0:
        Goran.append("B")

counts = [0,0,0]
for i in range(charLen):
    if answer[i] == Adrian[i]:
        counts[0] += 1
    if answer[i] == Bruno[i]:
        counts[1] += 1
    if answer[i] == Goran[i]:
        counts[2] += 1

max = 0
for i in counts:
    if i > max:
        max = i
print(max)

if counts[0] == max:
    print("Adrian")
if counts[1] == max:
    print("Bruno")
if counts[2] == max:
    print("Goran")