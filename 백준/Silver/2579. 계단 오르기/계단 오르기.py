import sys
input = sys.stdin.readline
from collections import deque
 
                
if __name__ == "__main__":
    n = int(input())
    values = [0] + [int(input()) for i in range(n)]
    if (n == 1 or n == 2):
        print(sum(values))
    else:
        dp = [0 for i in range(n+1)]
        dp[1] = values[1]
        dp[2] = values[1] + values[2]
        dp[3] = max(values[1] + values[3], values[2] + values[3])
        
        for i in range(4, n+1):
            dp[i] = max(dp[i-3] + values[i-1] + values[i], dp[i-2] + values[i])
            
        print(dp[n])