import sys
input = sys.stdin.readline
from collections import deque

if __name__ == "__main__":
    n, l = map(int, input().split())
    loc = list(map(int, input().split()))
    loc.sort()
    loc = deque(loc)
    answer = 0
    
    while loc:
        node = loc.popleft()
        length = node + l - 1
        while True:
            if (loc and loc[0] <= length): 
                loc.popleft()
            else: break
        answer += 1
        
    print(answer)
