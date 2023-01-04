from sys import stdin

l, p = map(int, stdin.readline().split())
a = stdin.readline().split()

for i in a:
    print(int(i)-(l*p), end=" ")