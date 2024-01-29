import sys
from collections import deque

input = sys.stdin.readline

global r, c
global matrix, visited, string

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]
maximum = 0

def dfs(y, x):
    global maximum, dy, dx
    
    maximum = max(maximum, len(string))
    
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if not (0 <= ny < r) or  not (0 <= nx < c): continue
        if visited[ny][nx][0]: continue
        if matrix[ny][nx] in string: continue
        if string == visited[ny][nx][1]: continue
        visited[ny][nx][1] = string[:]
        string.append(matrix[ny][nx])
        visited[ny][nx][0] = True
        dfs(ny, nx)
        string.pop()
        visited[ny][nx][0] = False
    
if __name__ == "__main__":
    r, c = map(int, input().split())
    matrix = []
    sys.setrecursionlimit(100000)
    
    for _ in range(r):
        matrix.append(list(input().strip()))
       
    visited = [[[False, []] for _ in range(c)] for _ in range(r)] 
    string = []
    string.append(matrix[0][0])
    
    dfs(0,0)
    
    print(maximum)