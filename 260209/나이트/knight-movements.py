import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
sy, sx, ey, ex = map(int, input().split())
sy -= 1
sx -= 1
ey -= 1
ex -= 1

dys = [-2, -2, -1, -1, 1, 1, 2, 2]
dxs = [-1, 1, -2, 2, -2, 2, -1, 1]

visited = [
        [False for _ in range(N)]
        for _ in range(N)
    ]
trace = [
        [-1 for _ in range(N)]
        for _ in range(N)
    ]

def inRange(y, x):
    return (0 <= y < N) and (0 <= x < N)

def canGo(y, x):
    return inRange(y, x) and not visited[y][x]

def bfs():

    deq = deque([(sy, sx)])
    visited[sy][sx] = True
    trace[sy][sx] = 0

    answer = -1

    while deq:

        cy, cx = deq.popleft()

        if (cy, cx) == (ey, ex):
            answer = trace[cy][cx]
            break

        for dy, dx in zip(dys, dxs):
            ny, nx = cy + dy, cx + dx
            if canGo(ny, nx):
                visited[ny][nx] = True
                trace[ny][nx] = trace[cy][cx] + 1
                deq.append((ny, nx))

    print(answer)
       

if __name__=="__main__":
    bfs()
