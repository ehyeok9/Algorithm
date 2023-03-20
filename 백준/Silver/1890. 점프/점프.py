import sys

global array
global answer
global n
global visited

def dp(y, x, cnt):
    global answer
    if (y < 0 or y >= n): return 0
    if (x < 0 or x >= n): return 0
    
    if (visited[y][x] != 0): return visited[y][x]
    if (y == n-1 and x == n-1): return 1
    if (array[y][x] == 0): return 0
    
    visited[y][x] = dp(y+array[y][x], x, cnt+1) + dp(y, x+array[y][x], cnt+1)
    return visited[y][x]
    
if __name__ == "__main__":
    n = int(sys.stdin.readline())
    array = []
    visited = [[0] * n for _ in range(n)]
    answer = 0
    for i in range(n):
        tmp = list(map(int, sys.stdin.readline().split()))
        array.append(tmp)
    print(dp(0, 0, 1))
    