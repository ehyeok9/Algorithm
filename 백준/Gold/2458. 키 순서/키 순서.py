import sys
from collections import deque

input = sys.stdin.readline

def bfs(graph, start):
    deq = deque([start])
    visited = set()
    
    while deq:
        node = deq.popleft()
        
        for nxt in graph[node]:
            if nxt not in visited:
                visited.add(nxt)
                deq.append(nxt)
    
    return len(visited)
            
if __name__ == "__main__":
    n, m = map(int, input().split())

    direct = [[] for _ in range(n+1)]
    undirect = [[] for _ in range(n+1)]
    for i in range(m):
        a, b = map(int, input().split())
        direct[a].append(b)
        undirect[b].append(a)
    
    result = 0
    for i in range(1, n+1):
        count = bfs(direct, i) + bfs(undirect, i) + 1
        
        if (count == n):
            result += 1
    print(result)
    