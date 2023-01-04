from sys import stdin

a = list(int(stdin.readline()) for i in range(10))
print(a[0]-sum(a[1:]))