import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().split()))
    
    dp = arr[:]
    
    for i in range(n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + arr[i])
            
    
    print(max(dp))
    
    
    
    