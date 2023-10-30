import sys
from collections import deque

input = sys.stdin.readline

n = int(input().rstrip())
arr = [list(map(int, input().split())) for _ in range(n)]
result = [[0 for _ in range(n)] for i in range(n)]
visited =  [False for _ in range(n)]

def dfs(x):
    for i in range(n):
        if (arr[x][i] == 1 and visited[i] == False):
            visited[i] = True
            dfs(i)
    
        
            
        
    
if __name__ == "__main__":
    for i in range(n):
        dfs(i)
        for j in range(n):
            if visited[j] == True:
                result[i][j] = 1
        visited =  [False for _ in range(n)]
                
    for i in range(n):
        print(*result[i])
            
    