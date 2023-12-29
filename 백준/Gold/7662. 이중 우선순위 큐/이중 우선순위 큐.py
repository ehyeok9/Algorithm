import sys
import heapq

input = sys.stdin.readline

if __name__ == "__main__":
    t = int(input())
    
    for i in range(t):
        k = int(input())
        
        min_heap = []
        max_heap = []
        deleted = [True] * k
        for j in range(k):
            command, val = map(str, input().split())
            val = int(val)
            
            if command == 'I':
                heapq.heappush(min_heap, (val, j))
                heapq.heappush(max_heap, (-val, j))
                deleted[j] = False
            else:
                if len(min_heap) == 0:
                    continue
                
                if val == -1:
                    while min_heap and deleted[min_heap[0][1]]:
                        heapq.heappop(min_heap)
                    if min_heap:
                        deleted[min_heap[0][1]] = True
                        heapq.heappop(min_heap)
                else:
                    while max_heap and deleted[max_heap[0][1]]:
                        heapq.heappop(max_heap)
                    if max_heap:
                        deleted[max_heap[0][1]] = True
                        heapq.heappop(max_heap)
            while min_heap and deleted[min_heap[0][1]]:
                heapq.heappop(min_heap)
            while max_heap and deleted[max_heap[0][1]]:
                heapq.heappop(max_heap)
                
        if not min_heap or not max_heap:
            print("EMPTY")
        else:
            print(-max_heap[0][0], min_heap[0][0])
                    
                     