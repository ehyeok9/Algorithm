import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
matrix = [
    list(map(int, input().split()))
    for _ in range(N)
]
startPoint = [
    list(map(int, input().split()))
    for _ in range(K)
]
visited = [
    [False for _ in range(N)]
    for _ in range(N)
]

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

answer = 0

def inRange(y, x):
    return (0 <= y < N) and (0 <= x < N)

def canGo(y, x):
    return matrix[y][x] == 0

def bfs(y, x):
    global answer

    deq = deque([(y, x)])
    visited[y][x] = True
    answer += 1

    while deq:
        y, x = deq.popleft()
        
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            
            if not inRange(ny, nx): continue
            if not canGo(ny, nx): continue
            if visited[ny][nx]: continue

            visited[ny][nx] = True
            answer += 1
            deq.append((ny, nx))

if __name__=="__main__":
    for y, x in startPoint:
        if not visited[y - 1][x - 1]:
            bfs(y - 1, x - 1)
    
    print(answer)