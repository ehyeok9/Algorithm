from sys import stdin

n = int(stdin.readline())
u = [[0,1]]

for i in range(1,n):
    q = [sum(u[i-1]), u[i-1][0]]
    u.append(q)

print(sum(u[len(u)-1]))