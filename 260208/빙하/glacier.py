import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [
    list(map(int, input().split()))
    for _ in range(N)
]

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

GRACIER = 1
WATER = 0

def inRange(y, x):
    return (0 <= y < N) and (0 <= x < M)

def bfs(y, x, visited):
    deq = deque([(y, x)])
    visited[y][x] = True
    area = set()

    while deq:
        cy, cx = deq.popleft()
        area.add((cy, cx))

        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]
            if not inRange(ny, nx): continue
            if visited[ny][nx]: continue
            if (matrix[ny][nx] != WATER): continue

            visited[ny][nx] = True
            deq.append((ny, nx))
    
    return area


def findWaterArea():
    visited = [
        [False for _ in range(M)]
        for _ in range(N)
    ]
    stack = []

    for y in range(N):
        for x in range(M):
            if not visited[y][x] and matrix[y][x] == WATER:
                area = bfs(y, x, visited)
                stack.append(area)
    
    return stack

def isExistGracier():
    for y in range(N):
        for x in range(M):
            if (matrix[y][x] == GRACIER):
                return True
    return False

def existInArea(area, y, x):
    return (y, x) in area

def isAroundGracier(area):
    for y, x in area:
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if not inRange(ny, nx): return False
            if matrix[ny][nx] == GRACIER: continue
            if existInArea(area, y, x): continue
            return False
    return True

def isAroundWater(y, x, curExceptedWater):
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        
        if not inRange(ny, nx): continue
        if curExceptedWater[ny][nx]: continue
        if matrix[ny][nx] == GRACIER: continue
    
        return True
    return False
def meltGracier(curExceptedWater):
    meltPos = []

    for y in range(N):
        for x in range(M):
            if (matrix[y][x] == GRACIER) and isAroundWater(y, x, curExceptedWater):
                meltPos.append((y, x))
    
    return meltPos
                

def simulation():
    time = 0
    meltCnt = 0
    
    while True:
        # 빙하가 있는지 확인
        if not isExistGracier():
            break
        
        # 빙하로 둘러싸인 물의 영역들 찾기
        stack = findWaterArea()
        curExceptedWater = [
            [False for _ in range(M)]
            for _ in range(N)
        ]
        
        for area in stack:
            if isAroundGracier(area):
                for y, x in area:
                    curExceptedWater[y][x] = True
        
        # 빙하 녹이기
        meltPos = meltGracier(curExceptedWater)
        
        time += 1
        meltCnt = len(meltPos)
        
        for y, x in meltPos:
            matrix[y][x] = WATER
                

    print(time, meltCnt)

        


if __name__=="__main__":
    simulation()
