import sys
input = sys.stdin.readline
from collections import deque

if __name__ == "__main__":
    n, m = map(int, input().split())
    loc = list(map(int, input().split()))
    deq = deque([num for num in range(1, n+1)])
    result = 0
    
    for location in loc:
        if (location == deq[0]):
            deq.popleft()
            continue
        
        direction = True
        target_loc = -1
        for i in range(len(deq)):
            if (deq[i] == location):
                target_loc = i
                break
        if (target_loc <= len(deq)//2):
            direction = False
        
        while True:
            if (location == deq[0]):
                deq.popleft()
                break
            if (direction):
                deq.appendleft(deq.pop())
            else:
                deq.append(deq.popleft())
            result += 1
            
    print(result)  
            