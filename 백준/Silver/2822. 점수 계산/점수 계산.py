from sys import stdin

u = list(int(stdin.readline()) for i in range(8))
k = sorted(u)

print(sum(k[3:]))

for i in range(3):
    u[u.index(k[i])] = -1

for i in u:
    if i != -1:
        print(u.index(i)+1, end=" ")