import sys
from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs(map, visited, row, col, mr, mc):
    deq = deque()
    ans = 0
    deq.append((row, col))
    visited[row][col] = True
    
    while(deq):
        node = deq.popleft()
        y = node[0]
        x = node[1]
        if (map[y][x] == 2): ans += 1
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if (ny < 0 or ny >= mr): continue
            if (nx < 0 or nx >= mc): continue
            if (visited[ny][nx]): continue
            if (map[ny][nx] == 1): continue
            deq.append((ny,nx))
            visited[ny][nx] = True
            
    if (ans == 0): return "TT"
    return ans

    
if __name__=="__main__":
    row, col = map(int, sys.stdin.readline().split())
    map = [sys.stdin.readline() for _ in range(row)]
    bi_map = []
    
    locy=-1; locx=-1
    for i in range(row):
        te = []
        for j in range(col):
            val = map[i][j]
            if (val == "O"): te.append(0)
            if (val == "X"): te.append(1)
            if (val == "P"): te.append(2)
            if (val == "I"):
                te.append(3)
                locy = i; locx=j
        bi_map.append(te)

    visited = [[False for j in range(col)] for i in range(row)]

    print(bfs(bi_map, visited, locy, locx, row, col))
    