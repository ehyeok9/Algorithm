from sys import stdin

while (True):
    u = list(map(int, stdin.readline().split()))
    if (len(u) == 1) and u[0] == -1:
        break
    cnt = 0
    for i in range(len(u)):
        for j in range(len(u)):
            if i == j:
                continue
            if u[j] == u[i]*2:
                cnt += 1
    print(cnt)