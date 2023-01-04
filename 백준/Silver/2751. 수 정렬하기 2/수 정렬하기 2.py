from sys import stdin
t = int(stdin.readline())

n = [int(stdin.readline()) for i in range(t)]

n.sort()

for i in range(len(n)):
    print(n[i])