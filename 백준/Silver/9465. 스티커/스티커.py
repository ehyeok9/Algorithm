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

if __name__ == "__main__":
    t = int(input().strip())
    
    for _ in range(t):
        n = int(input().strip())
        arr = []
        for i in range(2):
            arr.append(list(map(int, input().split())))
        
        result = dp(arr, n)
        
        print(result)
    
    
    
    