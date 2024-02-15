import sys
from collections import deque

input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    result = []
    
    deq = deque()
    for i in range(N):
        command = list(input().split())
        if len(command) == 2:
            deq.append(command[1])
        if command[0] == "pop":
            if len(deq) == 0:
                result.append("-1")
            else:
                result.append(deq.popleft())
        elif command[0] == "size":
            result.append(str(len(deq)))
        elif command[0] == "empty":
            if len(deq) == 0:
                result.append('1')
            else:
                result.append('0')
        elif command[0] == "front":
            if len(deq) == 0:
                result.append("-1")
                continue
            result.append(deq[0])
        elif command[0] == "back":
            if len(deq) == 0:
                result.append('-1')
                continue
            result.append(deq[-1])
        
    print("\n".join(result))