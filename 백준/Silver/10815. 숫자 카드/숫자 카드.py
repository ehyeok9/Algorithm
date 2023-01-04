from sys import stdin

n = int(stdin.readline())
nlit = sorted(list(map(int, stdin.readline().split())))
m = int(stdin.readline())
mlit = list(map(int, stdin.readline().split()))
result = []

for i in range(m):
    target = mlit[i]
    upper = len(nlit)-1
    lower = 0
    while True:
        middle = (upper+lower)//2
        if target == nlit[middle]:
            result.append(1)
            break
        elif target < nlit[lower] or target > nlit[upper]:
            result.append(0)
            break
        elif target > nlit[middle]:
            lower = middle+1
        elif target < nlit[middle]:
            upper = middle-1

for i in result:
    print(i, end=" ")