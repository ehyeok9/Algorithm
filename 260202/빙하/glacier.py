import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [
    list(map(int, input().split()))
    for _ in range(N)
]

GLACIER = 1
WATER = 0

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

def isGlacier(y, x):
    return matrix[y][x] == GLACIER

def isWater(y, x):
    return matrix[y][x] == WATER

def inRange(y, x):
    return (0 <= y < N) and (0 <= x < M)

def makeDeque():
    deq = deque()
    for y in range(N):
        for x in range(M):
            if isGlacier(y, x):
                deq.append((y, x))
    
    return deq

def getAroundWaterPosition(y, x):
    positions = []
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if not inRange(ny, nx): continue
        if isWater(ny, nx):
            positions.append((ny, nx))

    return positions

def isAllAroundGracier(y, x):
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if not inRange(ny, nx): continue
        if not isGlacier(ny, nx):
            return False
    return True
    
def bfs(deq):
    meltingGracier = deque()

    while deq:
        y, x = deq.popleft()

        waterPositions = getAroundWaterPosition(y, x)
        if (len(waterPositions) == 0): continue

        for wy, wx in waterPositions:
            isArroundGracier = isAllAroundGracier(wy, wx)

            if not isArroundGracier:
                meltingGracier.append((y, x))
                break
    
    return meltingGracier
        

def simulation():
    time = 0
    count = 0

    while True:
        deq = makeDeque()

        if (len(deq) == 0):
            break
        
        meltingGracier = bfs(deq)
        count = len(meltingGracier)
        time += 1

        for y, x in meltingGracier:
            matrix[y][x] = WATER

        # for line in matrix:
        #     print(*line)
    print(time, count)


if __name__=="__main__":
    simulation()