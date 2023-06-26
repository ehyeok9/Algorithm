import sys
from collections import deque

dy = [0,0,-1,1]
dx = [-1,1,0,0]

def bfs(input, result, visited, row, col, max_r, max_c):
    deq = deque()
    deq.append([(row, col), 0])
    visited[row][col] = True

    while deq:
        node = deq.popleft()
        y = node[0][0]
        x = node[0][1]
        idx = node[1]
        result[y][x] = idx
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if (ny < 0 or ny >= max_r): continue
            if (nx < 0 or nx >= max_c): continue
            if (visited[ny][nx] == True): continue
            if (input[ny][nx] == 0): continue
            deq.append([(ny,nx), idx+1])
            visited[ny][nx] = True
    
    for i in range(max_r):
        for j in range(max_c):
            if (input[i][j] == 1 and result[i][j] == 0):
                result[i][j] = -1
    
    
        

if __name__=="__main__":
    row, col = map(int, sys.stdin.readline().split())
    input = [
        list(map(int, sys.stdin.readline().split())) for _ in range(row)
    ]
    result = [[0 for j in range(col)] for i in range(row)]
    visited = [[False for j in range(col)] for i in range(row)]
    
    y= -1; x= -1
    for i in range(row):
        for j in range(col):
            if (input[i][j] == 2):
                y = i; x= j    
                
    bfs(input, result, visited, y, x, row, col)
    
    for i in range(row):
        print(*result[i])