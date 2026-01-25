import sys

input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [
    list(map(int, input().split()))
    for _ in range(N)
]
visited = []
maxK = 0

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

def makeVisited():
    global visited

    visited = [
        [False for _ in range(M)]
        for _ in range(N)
    ]

def findMaxK():
    global maxK

    val = float("-inf")

    for y in range(N):
        for x in range(M):
            val = max(val, matrix[y][x])
    
    maxK = val

def canGo(K, y, x):
    return matrix[y][x] > K

def inRange(y, x):
    return (0 <= y < N) and (0 <= x < M)

def dfs(K, y, x):
    
    visited[y][x] = True

    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        
        if not inRange(ny, nx): continue
        if not canGo(K, ny, nx): continue
        if visited[ny][nx]: continue

        dfs(K, ny, nx)

if __name__=="__main__":
    findMaxK()
    answer = []

    for K in range(1, maxK):
        makeVisited()
        safeZone = 0
        
        for y in range(N):
            for x in range(M):
                if canGo(K, y, x) and not visited[y][x]:
                    safeZone += 1
                    dfs(K, y, x)
        
        answer.append([K, safeZone])
    
    answer.sort(key=lambda x : (-x[1], x[0]))
    
    print(*answer[0])
        
    