import sys
input = sys.stdin.readline
from collections import deque
import copy

if __name__ == "__main__":
    n = int(input())
    loc = [list(input().rstrip()) for i in range(n)]
    loc2 = copy.deepcopy(loc)
    hori = 0
    for i in range(n):
        for j in range(n-1):
            if (loc[i][j] == '.' and loc[i][j+1] == '.'):
                hori += 1
                for k in range(j, n):
                    if (loc[i][k] == 'X'): break
                    loc[i][k] = 'X'
                
    verti = 0
    for i in range(n-1):
        for j in range(n):
            if (loc2[i][j] == '.' and loc2[i+1][j] == '.'):
                verti += 1
                for k in range(i, n):
                    if (loc2[k][j] == 'X'): break
                    loc2[k][j] = 'X'
    
    print(hori, verti)