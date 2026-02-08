import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [
    list(map(int, input().split()))
    for _ in range(N)
]

SNAKE = 0

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

answer = float("inf")

def inRange(y, x):
    return (0 <= y < N) and (0 <= x < M)

def bfs():
    global answer

    deq = deque([(0, 0, 0)])
    visited = [
        [False for _ in range(M)]
        for _ in range(N)
    ]
    visited[0][0] = True

    while deq:
        cy, cx, cnt = deq.popleft()

        if (cy, cx) == (N - 1, M - 1):
            answer = min(answer, cnt)

        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]
            
            if not inRange(ny, nx): continue
            if visited[ny][nx]: continue
            if matrix[ny][nx] == SNAKE: continue

            visited[ny][nx] = True
            deq.append((ny, nx, cnt + 1))



if __name__=="__main__":
    bfs()
    print(answer)
