import sys
import heapq

input = sys.stdin.readline

def floyd_warshall(graph, n):
    for k in range(n+1):
        for i in range(n+1):
            if graph[i][k] == float("inf"):
                continue
            for j in range(n+1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

def djikstra(graph, n, start):
    heap = []
    heapq.heappush(heap, (0, start))
    distance = [float("inf") for _ in range(n+1)]
    distance[start] = 0
    
    while heap:
        dist, node = heapq.heappop(heap)
        
        if distance[node] < dist: continue
        
        for time, nxt in graph[node]:
            cost = dist + time
            if cost < distance[nxt]:
                distance[nxt] = cost
                heapq.heappush(heap, (cost, nxt))
                
    return distance
    
if __name__ == "__main__":
    N, M, X = map(int, input().split())
    
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        start, end, time = map(int, input().split())
        graph[start].append((time, end))
    
    result = 0
    for i in range(1, N+1):
        toX = djikstra(graph, N, i)
        fromX = djikstra(graph, N, X)
        result = max(result, toX[X] + fromX[i])
    
    print(result)
    