m, n = list(map(int, input().split(" ")))
cols = [[] for _ in range(n)]

for _ in range(m):
    row = input()
    for i, v in enumerate(row):
        cols[i].append(v)

for i, col in enumerate(cols):
    p1 = 0
    while p1 < len(col):
        if col[p1] == '#':
            p1 += 1
            continue
        
        p2 = p1
        a_count = 0
        

        while p2 < len(col) and (col[p2] == '.' or col[p2] == 'a'):
            if col[p2] == 'a':
                a_count += 1
            p2 += 1
        
        # update block
        block_size = p2 - p1
        for j in range(p1, p2):
            if j < p1 + (block_size - a_count):
                cols[i][j] = '.'
            else:
                cols[i][j] = 'a'
        
        p1 = p2

rows = [[None for _ in range(n)] for _ in range(m)]

for j, s in enumerate(cols):
    for i, c in enumerate(s):
        rows[i][j] = c

for r in rows:
    print("".join(r))