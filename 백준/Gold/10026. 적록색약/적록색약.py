import sys
input = sys.stdin.readline
from collections import deque

dy = [0,0,-1,1]
dx = [-1,1,0,0]
dic = {'R': ['R', 'G'], 'G': ['R', 'G'], 'B': ['B']}
def bfs(visited, color, loc, length):
    deq = deque([loc])
    visited[loc[0]][loc[1]] = True
    
    while deq:
        node = deq.popleft()
        y = node[0]
        x = node[1]
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if (ny >= length or ny < 0 or nx >= length or nx < 0): continue
            if (visited[ny][nx] == True): continue
            if (color[y][x] != color[ny][nx]): continue
            deq.append((ny,nx))
            visited[ny][nx] = True
            
def bfs2(visited, color, loc, length):
    deq = deque([loc])
    visited[loc[0]][loc[1]] = True
    
    while deq:
        node = deq.popleft()
        y = node[0]
        x = node[1]
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if (ny >= length or ny < 0 or nx >= length or nx < 0): continue
            if (visited[ny][nx] == True): continue
            if (color[ny][nx] in dic[color[y][x]]):
                deq.append((ny,nx))
                visited[ny][nx] = True

if __name__ == "__main__":
    n = int(input())
    color = [list(input().rstrip()) for _ in range(n)]
    visited = [[False for j in range(n)] for i in range(n)]
    ct = 0
    cf = 0
    
    for i in range(n):
        for j in range(n):
            if (visited[i][j] == True): continue
            bfs(visited, color, (i,j), n)
            ct += 1
    
    visited = [[False for j in range(n)] for i in range(n)]
    
    for i in range(n):
        for j in range(n):
            if (visited[i][j] == True): continue
            bfs2(visited, color, (i,j), n)
            cf += 1
    print(ct, cf)