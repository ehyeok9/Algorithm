import sys
import heapq

input = sys.stdin.readline

def dijkstra(graph, start, distance):
    heap = [(0, start)]
    distance[start] = 0
    
    while heap:
        weight, loc = heapq.heappop(heap)
        
        if (distance[loc] < weight): continue
        
        for w,v in graph[loc]:
            if (distance[v] > weight + w):
                distance[v]  = weight + w
                heapq.heappush(heap, (distance[v], v))

if __name__ == "__main__":
    n = int(input())
    m = int(input())
    
    distance = [float('inf') for _ in range(n+1)]
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        start, end, cost = map(int, input().split())
        graph[start].append((cost, end))
    
    start, end = map(int, input().split())
    
    dijkstra(graph, start, distance)
    
    print(distance[end])
        