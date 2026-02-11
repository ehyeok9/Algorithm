import sys
from collections import deque

input = sys.stdin.readline

N, H, M = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(N)
]

SPOT = 3
PERSON = 2
WALL = 1
ROAD = 0

dys = [-1, 1, 0, 0]
dxs = [0, 0, -1, 1]

def inRange(y, x):
    return (0 <= y < N) and (0 <= x < N)

def canGo(y, x, visited):
    return inRange(y, x) and (visited[y][x] == -1) and (grid[y][x] != WALL)

def bfs(sy, sx):
    visited = [
        [-1 for _ in range(N)]
        for _ in range(N)
    ]
    visited[sy][sx] = 0

    deq = deque([(sy, sx)])
    
    while deq:
        cy, cx = deq.popleft()

        if grid[cy][cx] == SPOT:
            return visited[cy][cx]

        for dy, dx in zip(dys, dxs):
            ny, nx = cy + dy, cx + dx

            if canGo(ny, nx, visited):
                visited[ny][nx] = visited[cy][cx] + 1
                deq.append((ny, nx))

    return -1

def simulation():

    # 사람이 있는 위치를 찾는다
    startPos = []
    for y in range(N):
        for x in range(N):
            if grid[y][x] == PERSON:
                startPos.append((y, x))
    
    # 결과 출력용 리스트를 만든다
    answer = [
        [0 for _ in range(N)]
        for _ in range(N)
    ]

    # 각 시작위치에서 가장 가까운 공간을 찾는다
    for y, x in startPos:
        time = bfs(y, x)
        answer[y][x] = time

    # 결과 출력
    for row in answer:
        print(*row)

if __name__=="__main__":
    simulation()
    