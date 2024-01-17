import sys
import heapq

input = sys.stdin.readline

INF = int(1e9)

def bellmanFord(start, edges, n):
    distance = [INF for _ in range(n+1)]
    distance[start] = 0
    cycle = False
 
    for i in range(1, n+1):
        for edge in edges:
            cur, nxt, w = edge
            if (distance[nxt] > distance[cur] + w):
                distance[nxt] = distance[cur] + w
                if i == n:
                    return True
    return False
    

def findPath():
    N, M, W = map(int, input().split())
    edges = []
    
    for _ in range(M):
        S, E, T = map(int, input().split())
        edges.append((S, E, T))
        edges.append((E, S, T))
    
    for _ in range(W):
        S, E, T = map(int, input().split())
        edges.append((S, E, -T))
    
    
    if bellmanFord(1, edges, N):
        print("YES")
        return       
    
    print("NO")
        
if __name__ == "__main__":
    t = int(input())
    
    for _ in range(t):
        findPath()