from sys import stdin
from collections import Counter

n = int(stdin.readline())
u = {}

for i in range(n):
    q = int(stdin.readline())
    if q in u:
        u[q] += 1
    else:
        u[q] = 1

u = Counter(u).most_common()
if len(u) != 1:
    if u[0][1] == u[1][1]:
        p = []
        for i in range(len(u)):
            if u[0][1] == u[i][1]:
                p.append(u[i])
            else:
                break
        p.sort(key=lambda o : o[0])
        print(p[0][0])
    else:
        print(u[0][0])
else:
    print(u[0][0])