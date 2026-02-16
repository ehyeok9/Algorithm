import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(N)
]

dys = [-1, 1, 0, 0]
dxs = [0, 0, -1, 1]

SPOILED_MANDARIN = 2
MANDARIN = 1

def inRange(y, x):
    return (0 <= y < N) and (0 <= x < N)

def simulation():
    # 상한 귤 위치 찾기
    spoiled = []
    for y in range(N):
        for x in range(N):
            if (grid[y][x] == SPOILED_MANDARIN):
                spoiled.append((y, x))
    
    visited = [
        [-1 for _ in range(N)]
        for _ in range(N)
    ]
    for y, x in spoiled:
        visited[y][x] = 0

    deq = deque(spoiled)

    while deq:
        cy, cx = deq.popleft()

        for dy, dx in zip(dys, dxs):
            ny, nx = cy + dy, cx + dx

            if not inRange(ny, nx): continue
            if grid[ny][nx] != MANDARIN: continue
            if (visited[ny][nx] != -1) and (visited[ny][nx] < (visited[cy][cx] + 1)): continue
            
            visited[ny][nx] = visited[cy][cx] + 1
            deq.append((ny, nx))
    
    # 결과 배열 만들기
    answer = [
        [-1 for _ in range(N)]
        for _ in range(N)
    ]
    
    for y in range(N):
        for x in range(N):
            if (grid[y][x] == SPOILED_MANDARIN) or (grid[y][x] == MANDARIN):
                if (visited[y][x] == -1):
                    answer[y][x] = -2
                else:
                    answer[y][x] = visited[y][x]
    
    for row in answer:
        print(*row)

if __name__=="__main__":
    simulation()