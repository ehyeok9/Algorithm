from sys import stdin

n = int(stdin.readline())
a = list(map(int, stdin.readline().split()))

print(min(a), end=" ")
print(max(a))