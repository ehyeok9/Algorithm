from sys import stdin
from itertools import combinations

n, m = map(int, stdin.readline().split())
num = list(map(int, stdin.readline().split()))

u = list(combinations(num,3))
j = -1

for i in u:
	k = sum(i)
	if k == m:
		j = k
		break
	elif j < k and  k < m:
		j= k

print(j)