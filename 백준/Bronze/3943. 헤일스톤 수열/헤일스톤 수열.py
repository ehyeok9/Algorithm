from sys import stdin

def heil(n):
    op = n
    while n != 1:
        if n%2 == 0:
            n /= 2
        else:
            n = n*3 +1
        if n > op:
            op = n
    return int(op)

t = int(stdin.readline())
for i in range(t):
    print(heil(int(stdin.readline())))