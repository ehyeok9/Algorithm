def diffsort(n):
    a = []
    for i in range(n):
        q, w = map(int, input().split())
        a.append((q,w))
    a.sort()
    for j in a:
        print(str(j[0]) + " " + str(j[1]))
from sys import stdin
u = int(stdin.readline())
diffsort(u)