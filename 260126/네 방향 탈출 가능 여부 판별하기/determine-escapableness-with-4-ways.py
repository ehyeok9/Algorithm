import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [
    list(map(int, input().split()))
    for _ in range(N)
]
visited = [
    [False for _ in range(M)]
    for _ in range(N)
]

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

def inRange(y, x):
    return (0 <= y < N) and (0 <= x < M)

def bfs():
    answer = 0 

    deq = deque([(0, 0)])
    visited[0][0] = True

    while deq:
        y, x = deq.popleft()

        if (y == (N-1)) and (x == (M - 1)):
            answer = 1
            break

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]

            if not inRange(ny, nx): continue
            if (matrix[ny][nx] == 0): continue
            if visited[ny][nx]: continue
            
            visited[ny][nx] = True
            deq.append((ny, nx))
    
    print(answer)


if __name__=="__main__":
    bfs()
