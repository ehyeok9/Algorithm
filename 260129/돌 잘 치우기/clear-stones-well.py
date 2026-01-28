import sys
from collections import deque

input = sys.stdin.readline
ROCK = 1

N, K, M = map(int, input().split())
matrix = [
    list(map(int, input().split()))
    for _ in range(N)
]
startPoint = [
    list(map(int, input().split()))
    for _ in range(K)
]

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

def inRange(y, x):
    return (0 <= y < N) and (0 <= x < N)

def getCopyVisited(curVisited):
    return [
        [curVisited[y][x] for x in range(N)]
        for y in range(N)
    ]

def bfs(sy, sx):
    visited = [
        [False for _ in range(N)]
        for _ in range(N)
    ]
    visited[sy][sx] = True
    visitCnt = 1
    raiseCnt = 0

    deq = deque([(sy, sx, raiseCnt, visitCnt, visited)])

    while deq:
        y, x, curRaiseCnt, cutVisitCnt, curVisited = deq.popleft()
        visitCnt = max(visitCnt, cutVisitCnt)

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            
            if not inRange(ny, nx): continue
            # 해당 경로에서 이미 방문했다면 pass
            if curVisited[ny][nx]: continue

            nxtVisited = getCopyVisited(curVisited)
            nxtVisited[ny][nx] = True

            if (matrix[ny][nx] == ROCK) and (curRaiseCnt < M):
                deq.append((ny, nx, curRaiseCnt + 1, cutVisitCnt + 1, nxtVisited))    
            elif (matrix[ny][nx] != ROCK):
                deq.append((ny, nx, curRaiseCnt, cutVisitCnt + 1, nxtVisited))   
                
        

    return visitCnt

    
    

if __name__=="__main__":
    answer = 0

    for sy, sx in startPoint:
        count = bfs(sy - 1, sx - 1) 
        answer = max(answer, count)
    
    print(answer)