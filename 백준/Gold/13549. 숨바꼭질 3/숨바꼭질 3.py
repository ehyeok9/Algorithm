import sys
from collections import deque

input = sys.stdin.readline

def find(start, destination):
    deq = deque()
    deq.append((start, 0))
    visited = set()
    while deq:
        cur, cnt = deq.popleft()
        if (cur == destination):
            return cnt
        
        double = cur*2
        back = cur - 1
        forward = cur + 1
        
        if (double <= 100000 and double >= 0 and double not in visited):
            deq.append((double, cnt))
            visited.add(double)
        if (back <= 100000 and back >= 0 and back not in visited):
            deq.append((back, cnt+1))
            visited.add(back)
        if (forward <= 100000 and forward >= 0 and forward not in visited):
            deq.append((forward, cnt+1))
            visited.add(forward)
    
    return -1

if __name__ == "__main__":
    start, destination = map(int, input().split())
    
    print(find(start, destination))
    