from queue import PriorityQueue
import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    
    if (n == 1): print(0)
    else:
        pq = PriorityQueue()
        for i in range(n):
            tmp = int(sys.stdin.readline())
            pq.put(tmp)
        
        answer = 0
        while (pq.qsize() > 2):
            a = pq.get()
            b = pq.get()
            answer += a+b
            pq.put(a+b)
        
        a = pq.get()
        b = pq.get()
        answer += a+b
        print(answer)
    

    