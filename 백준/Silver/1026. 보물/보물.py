from sys import stdin

n = int(stdin.readline())
alit = list(map(int, stdin.readline().split()))
blit =list(map(int, stdin.readline().split()))

alit.sort(reverse=True)
ub = sorted(blit)
total = 0

for i in range(n):
    total += (alit[i]*ub[i])

print(total)