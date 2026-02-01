import sys
from collections import deque

input = sys.stdin.readline
ROCK = 1

N, K, M = map(int, input().split())
matrix = [
    list(map(int, input().split()))
    for _ in range(N)
]
startPoint = [
    list(map(int, input().split()))
    for _ in range(K)
]

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

answer = float("-inf")

def inRange(y, x):
    return (0 <= y < N) and (0 <= x < N)

def findMaxArea(rockAreas, rockAllowed):
    global answer

    visited = [
        [False for _ in range(N)]
        for _ in range(N)
    ]

    totalCnt = 0

    for sy, sx in startPoint:
        if not visited[sy - 1][sx - 1]:
            totalCnt += bfs(sy - 1, sx - 1, rockAreas, rockAllowed, visited)

    answer = max(answer, totalCnt)


def bfs(sy, sx, rockAreas, rockAllowed, visited):
    
    deq = deque([(sy, sx)])
    visited[sy][sx] = True

    count = 1

    while deq:

        y, x = deq.popleft()

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]

            if not inRange(ny, nx): continue
            if visited[ny][nx]: continue

            pos = (ny, nx)
            if (matrix[ny][nx] != ROCK) or (matrix[ny][nx] == ROCK and pos in rockAreas and rockAllowed[pos]):
                visited[ny][nx] = True
                deq.append(pos)

                count += 1

    return count


def backtracking(rockAreas, rockAllowed, raiseCnt):
    if (raiseCnt == M):
        findMaxArea(rockAreas, rockAllowed)
        return
    
    for pos in rockAreas:
        if not rockAllowed[pos]:
            rockAllowed[pos] = True
            findMaxArea(rockAreas, rockAllowed)
            backtracking(rockAreas, rockAllowed, raiseCnt + 1)
            rockAllowed[pos] = False
    


def simulation():
    rockAreas = []
    for y in range(N):
        for x in range(N):
            if (matrix[y][x] == ROCK):
                rockAreas.append((y, x))

    rockAllowed = {}
    for pos in rockAreas:
        rockAllowed[pos] = False

    backtracking(rockAreas, rockAllowed, 0)

    print(answer)
    

if __name__=="__main__":
    simulation()