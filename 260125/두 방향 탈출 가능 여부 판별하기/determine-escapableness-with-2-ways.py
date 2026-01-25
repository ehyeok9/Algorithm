import sys

input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [
    list(map(int, input().split()))
    for _ in range(N)
]
dy = [0, 1]
dx = [1, 0]
visited = [
    [False for _ in range(M)]
    for _ in range(N)
]
answer = 0;

def inRange(y, x):
    return (0 <= y < N) and (0 <= x < M)

def canGo(y, x):
    return matrix[y][x] != 0

def dfs(y, x):
    global answer

    if (y == (N - 1)) and (x == (M - 1)):
        answer = 1
        return

    visited[y][x] = True

    for i in range(2):
        ny, nx = y + dy[i], x + dx[i]
        if not inRange(ny, nx): continue
        if not canGo(ny, nx): continue
        if visited[ny][nx]: continue

        dfs(ny, nx)

if __name__=="__main__":
    dfs(0, 0)

    print(answer)