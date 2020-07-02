winningSchools = []
for _ in range(int(input())):
    team = tuple(map(str, input().split()))
    if team[0] not in winningSchools and len(winningSchools) < 12:
        winningSchools.append(team[0])
        print(team[0] + " " + team[1])
