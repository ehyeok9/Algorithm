import sys
from collections import deque

input = sys.stdin.readline

global N, M, matrix

def melt():
    stack = []
    
    for i in range(N):
        for j in range(M):
            if (matrix[i][j] == 0): continue
            if (check(i,j)):
                stack.append((i,j))
    
    if stack == []:
        return 0
    
    for i,j in stack:
        matrix[i][j] = 0
    
    return 1

dy = [0,0,-1,1]
dx = [1,-1,0,0]

def check(y, x):
    count = 0
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if not (0 <= ny < N and 0 <= nx < M): continue
        if matrix[ny][nx] == 0:
            if (bfs(ny,nx)):
                count += 1
    
    if count < 2: 
        return False
    return True
    
def bfs(y, x):
    deq = deque()
    deq.append((y,x))
    visited = [[False for _ in range(M)] for _ in range(N)]
    visited[y][x] = True        
    flag = False
    
    while deq:
        curY, curX = deq.popleft()
        if curY == 0 or curY == N-1 or curX == 0 or curX == M-1:
            flag = True
            break
        
        for i in range(4):
            ny, nx = curY + dy[i], curX + dx[i]
            if not (0 <= ny < N and 0 <= nx < M): continue
            if matrix[ny][nx] == 1: continue
            if visited[ny][nx]: continue
            deq.append((ny,nx))
            visited[ny][nx] = True
    
    return flag
            
            
                
if __name__ == "__main__":
    N, M = map(int, input().split())
    matrix = []
    for _ in range(N):
        matrix.append(list(map(int, input().split())))
    
    result = 0
    while melt():
        result += 1
    
    print(result)
    
    