import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
matrix = [
    list(map(int, input().split()))
    for _ in range(N)
]
visited = [
    [False for _ in range(N)]
    for _ in range(N)
]

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

def inRange(y, x):
    return (0 <= y < N) and (0 <= x < N)

def canGo(y, x, stdVal):
    return matrix[y][x] == stdVal

def dfs(y, x, stdVal, count):
    
    visited[y][x] = True

    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        
        if not inRange(ny, nx): continue
        if not canGo(ny, nx, stdVal): continue
        if visited[ny][nx]: continue

        count = dfs(ny, nx, stdVal, count + 1)
    
    return count



if __name__=="__main__":
    blocks = []

    for y in range(N):
        for x in range(N):
            if not visited[y][x]:
                count = dfs(y, x, matrix[y][x], 1)
                blocks.append(count)
                    
    bomb = 0
    for block in blocks:
        if (block >= 4):
            bomb += 1
            
    print(bomb, max(blocks))
