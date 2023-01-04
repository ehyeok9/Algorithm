from sys import stdin

n = int(stdin.readline())
a = list(map(int, stdin.readline().split()))
a.sort()
total = 0

for i in range(len(a)):
    total += sum(a[:i+1])

print(total)