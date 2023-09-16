import sys
input = sys.stdin.readline
from collections import deque
import math

if __name__ == "__main__":
    n, k = map(int, input().split())
    result = []
    
    for i in range(1, int(math.sqrt(n))+1):
        if (n%i == 0):
            if (pow(i,2) == n): result.append(i)
            else:
                result.append(i)
                result.append(n//i)
    result.sort()
    
    if (len(result) < k): print(0)
    else: print(result[k-1])