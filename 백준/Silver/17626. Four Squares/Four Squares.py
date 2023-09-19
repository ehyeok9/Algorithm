import sys
input = sys.stdin.readline
from collections import deque
import math
                
if __name__ == "__main__":
    n = int(input())

    dp = [0 for i in range(n+1)]
    arr = []
    for i in range(1, int(math.sqrt(n)) + 1):
        dp[pow(i,2)] = 1
        arr.append(pow(i,2))
    
    pointer = 0
    for i in range(2, n+1):
        if (dp[i] == 1):
            pointer += 1
        else:
            temp = 4
            for j in range(pointer, pointer//2-1, -1):
                val = dp[i - arr[j]] + dp[arr[j]]
                if (val < temp): temp = val
                if temp == 2:
                    break
            dp[i] = temp
    print(dp[-1])
        