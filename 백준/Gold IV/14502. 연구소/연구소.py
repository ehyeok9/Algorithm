import sys
from collections import deque

input = sys.stdin.readline

global N, M, matrix
global walls

dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]

def chooseWalls(wall, visited, prev):
    if len(wall) == 3:
        walls.append(wall[:])
        return
    
    for i in range(prev, N * M):
        y, x = i//M, i%M
        if matrix[y][x] == 0:
            wall.append((y,x))
            chooseWalls(wall, visited, prev)
            wall.pop()          
        
def bfs(wall, start, total):      
    visited = [[False for _ in range(M)] for _ in range(N)]    
    deq = deque()
    for i in range(len(start)):
        deq.append(start[i])
        visited[start[i][0]][start[i][1]] = True
    for loc in wall:
        visited[loc[0]][loc[1]] = True
        
    count = 0
    while deq:
        y, x = deq.popleft()
        
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if not (0 <= ny < N and 0 <= nx < M): continue
            if matrix[ny][nx] == 1: continue
            if visited[ny][nx]: continue
            visited[ny][nx] = True
            count += 1
            deq.append((ny, nx))
    
    return total - count - 3
        
    
    
if __name__ == "__main__":
    N, M = map(int, input().split())
    
    matrix = []
    for i in range(N):
        matrix.append(list(map(int, input().split())))

    visited = [[False for _ in range(M)] for _ in range(N)]    
    walls = []
    chooseWalls([], visited, 0)

    start = []
    total = 0
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 2:
                start.append((i,j))
            if matrix[i][j] == 0:
                total += 1
    result = 0
    
    for wall in walls:
        result = max(bfs(wall, start, total), result)
        
    print(result)