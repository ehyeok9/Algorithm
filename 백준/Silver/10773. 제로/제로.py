from sys import stdin

k = int(stdin.readline())
u = []

for i in range(k):
    q = int(stdin.readline())
    if q == 0:
        u.pop()
    else:
        u.append(q)

print(sum(u))