import sys
from queue import PriorityQueue



if __name__=="__main__":
    n = int(sys.stdin.readline())
    pq = PriorityQueue()
    
    for i in range(n):
        num = int(sys.stdin.readline())
        if (num == 0):
            if (pq.empty()): print(0)
            else: print(pq.get()[1])
        else:
            pq.put((abs(num), num))