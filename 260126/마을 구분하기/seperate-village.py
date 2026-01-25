import sys

input = sys.stdin.readline

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

def canGo(y, x):
    return matrix[y][x] == 1

def dfs(y, x, count):

    visited[y][x] = True

    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        
        if not inRange(ny, nx): continue
        if not canGo(ny, nx): continue
        if visited[ny][nx]: continue
        
        count = dfs(ny, nx, count + 1)
    
    return count

if __name__=="__main__":
    village = []

    for y in range(N):
        for x in range(N):
            if not visited[y][x] and canGo(y, x):
                count = dfs(y, x, 1)
                village.append(count)
    
    village.sort()
    
    print(len(village))
    print(*village, sep="\n")
                