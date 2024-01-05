import sys

input = sys.stdin.readline

def dp(arr, n):
    memo = [[0 for _ in range(n)] for _ in range(2)]
    memo[0][0] = arr[0][0]
    memo[1][0] = arr[1][0]

    for i in range(1,n):
        memo[0][i] = max(memo[0][i-1], memo[1][i-1]+arr[0][i])
        memo[1][i] = max(memo[1][i-1], memo[0][i-1]+arr[1][i])
        
    return max(memo[0][n-1], memo[1][n-1])

def painting(color, n):
    memo = [[0 for _ in range(3)] for _ in range(n)]
    memo[0][0] = color[0][0]
    memo[0][1] = color[0][1]
    memo[0][2] = color[0][2]
    
    for i in range(n):
        memo[i][0] = min(memo[i-1][1], memo[i-1][2]) + color[i][0]
        memo[i][1] = min(memo[i-1][0], memo[i-1][2]) + color[i][1]
        memo[i][2] = min(memo[i-1][0], memo[i-1][1]) + color[i][2]
    
    return  min(memo[n-1][0], memo[n-1][1], memo[n-1][2])

if __name__ == "__main__":
    n = int(input())
    color = []
    for i in range(n):
        color.append(list(map(int, input().split())))
    
    print(painting(color, n))
    
    
    
    
    
    
    