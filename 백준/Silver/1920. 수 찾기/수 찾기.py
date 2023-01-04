from sys import stdin


n = int(stdin.readline())
nlit = sorted(list(map(int, stdin.readline().split())))
m = int(stdin.readline())
mlit = list(map(int, stdin.readline().split()))
result = []

for i in range(len(mlit)):
    target = mlit[i]
    lower = 0
    upper = len(nlit)-1
    while (True):
        middle = (upper+lower)//2
        if nlit[middle] == target :
            result.append(1)
            break
        elif (target > nlit[upper] or target < nlit[lower] ):
            result.append(0)
            break
        elif nlit[middle] > target:
            upper = middle-1
        elif nlit[middle] < target:
            lower = middle+1

for i in result:
    print(i)
