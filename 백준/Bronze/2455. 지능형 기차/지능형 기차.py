from sys import stdin

n = [list(map(int, stdin.readline().split())) for i in range(4)]
q = []

total = 0
for i in range(len(n)):
    total -= n[i][0]
    if total < 0:
        total = 0
    q.append(total)
    total += n[i][1]
    if total > 10000:
        total = 10000
    q.append(total)
print(max(q))