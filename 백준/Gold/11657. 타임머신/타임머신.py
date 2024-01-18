import sys
import heapq

input = sys.stdin.readline

INF = float('inf')

def bellmanFord(start, edges, n):
    distance = [INF for _ in range(n+1)]
    distance[start] = 0
 
    for i in range(1, n+1):
        for edge in edges:
            cur, nxt, w = edge
            if (distance[nxt] > distance[cur] + w):
                distance[nxt] = distance[cur] + w
                if i == n:
                    return True, []
    return False, distance
        
if __name__ == "__main__":
    n, m = map(int, input().split())
    edges = []
    
    for _ in range(m):
        a,b,c = map(int, input().split())
        edges.append((a,b,c))
    
    flag, distance = bellmanFord(1, edges, n)
    if flag:
        print(-1)
    else:
        for i in range(2, n+1):
            if distance[i] == INF:
                print(-1)
            else:
                print(distance[i])
        
            
    