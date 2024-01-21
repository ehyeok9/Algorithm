import sys
from collections import deque

input = sys.stdin.readline


def goRight(y, x):
    return [[y, x+1]]

def goDown(y, x):
    return [[y+1, x]]

def goRightDown(y, x):
    return [[y, x+1], [y+1, x], [y+1, x+1]]

def check(distance, n, home):
    for y,x in distance:
        if y >= n or x >= n:
            return False
        if home[y][x] == 1:
            return False
        
    return True

direction = {
    0: [goRight, goRightDown],
    1: [goDown, goRightDown],
    2: [goRight, goDown, goRightDown]
}

getKey = {
    goRight: 0,
    goDown: 1,
    goRightDown: 2
}

def bfs(home, n):
    deq = deque()
    deq.append([(0, 1), 0])
    visited = [[False for _ in range(n)] for _ in range(n)]
    visited[0][1] = True
    count = 0
    
    while deq:
        cur, direct = deq.popleft()
        y, x = cur
            
        if y == n-1 and x == n-1:
            count += 1
            continue
        
        for command in direction[direct]:
            distance = command(y, x)
            ny, nx = distance[-1]
            if check(distance, n, home):
                deq.append([distance[-1], getKey[command]])
    
    print(count)
    
    
def dp(home, n):
    memo = [[[0 for _ in range(3)] for _ in range(n)] for _ in range(n)]
    memo[0][1][0] = 1
    for i in range(2,n):
        if home[0][i] == 1: break
        memo[0][i][0] = 1
    
    for y in range(1,n):
        for x in range(1,n):            
            if home[y][x] == 0 and home[y][x-1] == 0 and home[y-1][x] == 0:
                memo[y][x][2] = memo[y-1][x-1][0] + memo[y-1][x-1][1] + memo[y-1][x-1][2]
            
            if home[y][x] == 0:
                memo[y][x][0] = memo[y][x-1][0] + memo[y][x-1][2]
                memo[y][x][1] = memo[y-1][x][1] + memo[y-1][x][2]
    
    print(sum(memo[n-1][n-1]))
            
    
                      
    

if __name__ == "__main__":
    n = int(input())
    
    home = []
    for _ in range(n):
        home.append(list(map(int, input().split())))
    
    dp(home, n)