from sys import stdin

def plus(n):
    lit = [0,1,2,4]
    if n < 4:
        return lit[n]
    else:
        for i in range(4,n+1):
            lit.append(lit[i-1]+lit[i-2]+lit[i-3])
        return lit.pop()

t = int(stdin.readline())

for i in range(t):
    n = int(stdin.readline())
    print(plus(n))