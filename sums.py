for _ in range(int(input())):
    K, N = map(int, input().split())
    q = N + N**2
    print(str(K), str(int(q/2)), str(int(N**2)), str(int(q)))