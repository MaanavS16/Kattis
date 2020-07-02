inBuilding = []
for _ in range(int(input())):
    event = tuple(map(str, input().split()))
    out = event[1]
    if event[0] == "entry":
        out += " entered"
        if event[1] in inBuilding:
            out += " (ANOMALY)"
        else:
            inBuilding.append(event[1])
    if event[0] == "exit":
        out += " exited"
        if event[1] not in inBuilding:
            out += " (ANOMALY)"
        else:
            inBuilding.remove(event[1])
    print(out)