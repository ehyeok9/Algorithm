from sys import stdin

n = int(stdin.readline())
u = [1,2]

if n <= 2:
    print(u[n-1])
else:
    for i in range(2,n):
        u.append(u[i-1] +u[i-2])
    print((u[n-1])%10007)