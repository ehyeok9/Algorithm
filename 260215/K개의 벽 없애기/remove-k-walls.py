import sys
from collections import deque

input = sys.stdin.readline

WALL = 1

N, K = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(N)
]
r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())

dys = [-1, 1, 0, 0]
dxs = [0, 0, -1, 1]

answer = float("inf")

def inRange(y, x):
    return (0 <= y < N) and (0 <= x < N)

def bfs(selected):
    visited = [
        [-1 for _ in range(N)]
        for _ in range(N)
    ]
    visited[r1 - 1][c1 - 1] = 0

    deq = deque([(r1 - 1, c1 - 1)])

    while deq:
        
        cy, cx = deq.popleft()

        if (cy, cx) == (r2 - 1, c2 - 1):
            break
        
        for dy, dx in zip(dys, dxs):
            ny, nx = cy + dy, cx + dx

            if not inRange(ny, nx): continue
            if (visited[ny][nx] != -1): continue
            if (grid[ny][nx] == WALL) and ((ny, nx) not in selected): continue

            visited[ny][nx] = visited[cy][cx] + 1
            deq.append((ny, nx))
    
    return visited[r2 - 1][c2 - 1]

def combination(idx, walls, visited, selected):
    global answer

    if (len(selected) == K):
        time = bfs(selected)
        if (time != -1):
            answer = min(answer, time)
            
        return
    
    for i in range(idx, len(walls)):
        if not visited[i]:
            visited[i] = True
            selected.append(walls[i])
            combination(i, walls, visited, selected)
            selected.pop()
            visited[i] = False
            

def simulation():
    global answer 
    # 벽 찾기
    walls = []
    for y in range(N):
        for x in range(N):
            if (grid[y][x] == WALL):
                walls.append((y, x))

    # 조합
    visited = [False for _ in range(len(walls))]
    combination(0, walls, visited, [])

    if answer == float("inf"):
        print(-1)
    else:
        print(answer)

if __name__=="__main__":
    simulation()