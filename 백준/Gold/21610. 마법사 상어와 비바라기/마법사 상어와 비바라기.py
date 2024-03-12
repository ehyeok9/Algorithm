import sys
from collections import deque

input = sys.stdin.readline

dy = [0, 0,-1,-1,-1,0,1,1,1]
dx = [0, -1,-1,0,1,1,1,0,-1]

global n, m, cloud

def water(board, d, s):
    global n, m, cloud
    
    # 구름 이동
    for i in range(len(cloud)):
        cloud[i][0] += dy[d] * s 
        cloud[i][1] += dx[d] * s 
    
    # 인덱스 잡기
    for i in range(len(cloud)):
        cloud[i] = getPosition(cloud[i], n)
    
    # 물 증가
    for y,x in cloud:
        board[y][x] += 1
    
    # 물복사버그 마법
    for pos in cloud:
        increase = copy(board, pos, n)
        board[pos[0]][pos[1]] += increase
    
    # 다음 구름 찾기
    visited = [[False for _ in range(n+1)] for _ in range(n+1)]
    while cloud:
        y,x = cloud.popleft()
        visited[y][x] = True
    
    for i in range(1, n+1):
        for j in range(1, n+1):
            if board[i][j] >= 2 and visited[i][j] == False:
                cloud.append([i,j])
                board[i][j] -= 2
    
    
    # printArr(board)
    
            
def printArr(board):
    for i in range(len(board)):
        print(*board[i])
    print()
        
        
def copy(board, pos, n):
    cy = [-1, -1, 1, 1]
    cx = [-1, 1, -1, 1]
    
    y, x = pos
    result = 0
    for i in range(4):
        ny, nx = y + cy[i], x + cx[i]
        if not (0 < ny <= n): continue
        if not (0 < nx <= n): continue
        if board[ny][nx] <= 0: continue
        result += 1
    
    return result
    

def getPosition(pos, n):
    y, x = pos

    if y <= 0: y = n - (abs(y)%n)
    elif y > n: 
        if y%n == 0: y = n
        else: y %= n
    
    if x <= 0: x = n - (abs(x)%n)
    elif x > n:
        if x%n == 0: x = n
        else: x %= n
    
    return [y,x]


if __name__ == "__main__":
    n, m = map(int, input().split())
    
    board = []
    for i in range(n):
        board.append(list(map(int, input().split())))
    
    board.insert(0, [0 for i in range(n)])
    for i in range(1,n+1):
        board[i].insert(0,0)

    cloud = deque([[n,1], [n,2], [n-1,1], [n-1,2]])
    for i in range(m):
        d, s = map(int, input().split())
        
        water(board, d, s)
        
    total = 0
    for i in range(1, n+1):
        total += sum(board[i])
    
    print(total)
    