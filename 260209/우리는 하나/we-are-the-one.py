import sys
from collections import deque

input = sys.stdin.readline

N, K, U, D = map(int, input().split())
matrix = [
    list(map(int, input().split()))
    for _ in range(N)
]
dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

maxCityCnt = float("-inf")

def canGo(fr, to):
    return (U <= abs(fr - to) <= D)

def inRange(y, x):
    return (0 <= y < N) and (0 <= x < N)

def bfs(cities):
    global maxCityCnt

    deq = deque(cities)
    visited = [
        [False for _ in range(N)]
        for _ in range(N)
    ]
    for y, x in cities:
        visited[y][x] = True
    count = len(cities)

    while deq:
        cy, cx = deq.popleft()

        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]

            if not inRange(ny, nx): continue
            if visited[ny][nx]: continue
            # print(f"{U} <= {matrix[cy][cx]} - {matrix[ny][nx]} <= {D}")
            if not canGo(matrix[cy][cx], matrix[ny][nx]): continue
            
            count += 1
            visited[ny][nx] = True
            deq.append((ny, nx))

    # print(f"{cities} -> count = {count}")
    maxCityCnt = max(maxCityCnt, count)

def backtracking(idx, flatten, cities):
    if (len(cities) == K):
        bfs(cities)
        return
    
    for i in range(idx, len(flatten)):
        cities.append(flatten[i])
        backtracking(i, flatten, cities)
        cities.pop()
    

def simulation():
    
    # 위치 좌표를 1차원 배열로 변형
    flatten = []

    for y in range(N):
        for x in range(N):
            flatten.append((y, x))
    
    backtracking(0, flatten, [])
    

    print(maxCityCnt)

if __name__=="__main__":
    simulation()