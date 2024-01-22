import sys
import heapq

input = sys.stdin.readline

def dijkstra(graph, n, start, end):
    distance = [float('inf')] * (n+1)
    distance[start] = 0
    heap = []
    heapq.heappush(heap, (0, start))
    history = [[] for _ in range(n+1)]
    history[start].append(start)
    
    while heap:
        # print(heap)
        dist, cur = heapq.heappop(heap)
        
        if (dist > distance[cur]): continue
        
        for nxt, cost in graph[cur]:
            temp = cost + dist
            if (temp < distance[nxt]):
                distance[nxt] = temp
                heapq.heappush(heap, (temp, nxt))
                history[nxt] = history[cur] + [nxt]
    
    print(distance[end])
    print(len(history[end]))
    print(*history[end])
    
if __name__ == "__main__":
    n = int(input())
    m = int(input())
    
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        start, end, cost = map(int, input().strip().split())
        graph[start].append((end, cost))
        
    start, end = map(int, input().strip().split())
        
    dijkstra(graph, n, start, end)