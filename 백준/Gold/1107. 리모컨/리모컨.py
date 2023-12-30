import sys
from collections import deque

input = sys.stdin.readline

def available(num, broken):
    cnt = 0
    if (num == 0):
        if 0 in broken:
            return False, -1
        else:
            return True, 1
    while num > 0:
        if num % 10 in broken:
            return False, -1
        num //= 10
        cnt += 1
    return True, cnt
    
def getMinimum(channel, broken):
    startMin = abs(channel - 100)
    result = startMin
    for num in range(1000001):
        flag, cnt = available(num, broken)
        if flag:
            distance = abs(channel - num) + cnt
            result = min(result, distance)
    return result
            
            
        

if __name__ == "__main__":
    channel = int(input())
    m = int(input())
    broken = list(map(int, input().split()))
    
    print(getMinimum(channel, broken))