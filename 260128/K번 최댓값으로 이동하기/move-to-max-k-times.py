import sys
from collections import deque 

input = sys.stdin.readline

N, K = map(int, input().split())
matrix = [
    list(map(int, input().split()))
    for _ in range(N)
]
sy, sx = map(int, input().split())
dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

visited = []
def inRange(y, x):
    return (0 <= y < N) and (0 <= x < N)

def makeVisitedList():
    global visited

    visited = [
        [False for _ in range(N)]
        for _ in range(N)
    ]

def getNextNumber(y, x):
    deq = deque([(y, x)])
    visited[y][x] = True
    number = matrix[y][x]
    nxtNumber = None

    while deq:
        stdY, stdX = deq.popleft()
        
        for i in range(4):
            ny, nx = stdY + dy[i], stdX + dx[i]
            
            if not inRange(ny, nx): continue
            if (matrix[ny][nx] >= number): continue
            if visited[ny][nx]: continue

            visited[ny][nx] = True
            deq.append((ny, nx))
            if nxtNumber is None:
                nxtNumber = matrix[ny][nx]
            else:
                nxtNumber = max(nxtNumber, matrix[ny][nx])
    
    return nxtNumber

def getNextPosition(number):
    for y in range(N):
        for x in range(N):
            if (matrix[y][x] == number) and visited[y][x]:
                return (y, x)
    return None

def printVisited():
    global visited

    for line in visited:
        print(*line)
    
def simulation():
    cy, cx = sy - 1, sx - 1
    
    for k in range(K):
        makeVisitedList()

        number = getNextNumber(cy, cx)
        if number is None: break

        nextPos = getNextPosition(number)
        if nextPos is None: break
        # print(f"{(cy, cx)} 에서 {number} 숫자를 가진 {nextPos}로 이동")
        # printVisited()
        cy, cx = nextPos
    
    print(cy + 1, cx + 1)

if __name__=="__main__":
    simulation()