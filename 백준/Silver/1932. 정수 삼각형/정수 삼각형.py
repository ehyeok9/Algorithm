import sys

input = sys.stdin.readline

def dp(triangle, n):
    memo = [[0 for _ in range(i+1)] for i in range(n)]
    memo[0][0] = triangle[0][0]
    
    for i in range(1,n):
        for j in range(i+1):
            if (j == 0):
                memo[i][j] = triangle[i][j] + memo[i-1][j]
            elif (j == i):
                memo[i][j] = triangle[i][j] + memo[i-1][j-1]
            else:
                memo[i][j] = max(memo[i-1][j-1], memo[i-1][j]) + triangle[i][j] 

    return max(memo[n-1])
if __name__ == "__main__":
    n = int(input())
    triangle = []
    for i in range(n):
        triangle.append(list(map(int, input().split())))
    
    print(dp(triangle, n))
    
    
    
    
    
    
    