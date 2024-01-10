import sys
import heapq

input = sys.stdin.readline

def dijkstra(graph, start, path):
    heap = [(0, start)]
    path[start] = 0
    
    while heap:
        weight, node = heapq.heappop(heap)
        
        if weight > path[node]: continue
        if node not in graph: continue
        for w, v in graph[node]:
            cost = weight + w
            if cost < path[v]:
                path[v] = cost
                heapq.heappush(heap, (cost, v))        
                
                
if __name__ == "__main__":
    n,m = map(int, input().split())
    start = int(input())
    graph = dict()
    path = [float("inf") for _ in range(n+1)]
    
    for _ in range(m): 
        u, v, w = map(int, input().split())
        if u not in graph: graph[u] = [(w, v)]
        else: graph[u].append((w, v))
    
    dijkstra(graph, start, path)
    
    for i in range(1, n+1):
        if path[i] == float("inf"):
            sys.stdout.write("INF\n")
        else:
            sys.stdout.write("%d\n" % path[i])
        