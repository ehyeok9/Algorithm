import math
import sys
from collections import deque

def eratos(end):
    answer = 0
    for i in range(1, int(math.sqrt(end))):
        if (end%i == 0):
            answer+= 2
    return answer

if __name__ == "__main__":
    l, r = map(int, sys.stdin.readline().split())
    
    res = 0
    for i in range(l, r+1):
        if (i == l):
            res += i
            continue
        val = eratos(i)
        res += (i-val)
        
    print(res)

        