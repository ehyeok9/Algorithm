from sys import stdin

n,m = map(int, stdin.readline().split())

narray = list(map(int, stdin.readline().split()))
marray = list(map(int, stdin.readline().split()))

for i in sorted(marray+narray):
    print(i, end=" ")