from sys import stdin

n = int(stdin.readline())
lit = list(map(int, stdin.readline().split()))

if lit == sorted(lit, reverse=True):
    print(-1)
else:
    for i in range(len(lit)-1, 0,-1):
        if lit[i-1] < lit[i]:
            qq = i-1
            break

    for i in range(len(lit)-1, 0 , -1):
        if lit[i] > lit[qq]:
            pp = i
            break
    lit[qq], lit[pp] = lit[pp], lit[qq]
    lit2 = lit[:qq+1]
    lit = sorted(lit[qq+1:])
    lit2 += lit
    for i in lit2:
        print(i, end=" ")