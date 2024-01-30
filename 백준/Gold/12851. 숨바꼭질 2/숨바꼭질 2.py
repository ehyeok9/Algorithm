import sys
from collections import deque

input = sys.stdin.readline

global N, K

def bfs():
    deq = deque()
    visited = [[0, 0] for _ in range(100001)]
    deq.append(N)
    
    
    while deq:
        cur = deq.popleft()
        
        if cur == K:
            visited[cur][1] += 1
            continue
        
        for nxt in [cur-1, cur+1, cur*2]:
            if not (0 <= nxt <= 100000): continue
            if visited[nxt][0] == 0 or visited[cur][0] + 1 == visited[nxt][0]:
                # print(nxt)
                visited[nxt][0] = visited[cur][0] + 1 
                deq.append(nxt)
    
    
    print(visited[K][0])
    print(visited[K][1])
            
                
if __name__ == "__main__":
    
    N, K = map(int, input().split())
    
    bfs()