import sys
import heapq

input = sys.stdin.readline

def dijkstra(graph, start, n, next):
    distance = [float('inf') for _ in range(n+1)]
    heap = [(0, start)]
    distance[start] = 0
    
    while heap:
        weight, loc = heapq.heappop(heap)
        
        if distance[loc] < weight: continue
        
        for w,v in graph[loc]:
            if (distance[v] > weight + w):
                distance[v] = weight + w
                heapq.heappush(heap, (distance[v], v))
    # print(distance)
    return distance[1], distance[next], distance[n]
    

if __name__ == "__main__":
    n, e = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    
    for _ in range(e):
        v1, v2, cost = map(int, input().split())
        graph[v1].append((cost, v2))
        graph[v2].append((cost, v1))
        
    v1, v2 = map(int, input().split())
    
    v1_1, v1_v2, v1_n = dijkstra(graph, v1, n, v2)
    v2_1, v2_v1, v2_n = dijkstra(graph, v2, n, v1)
    ans1 = v1_1 + v1_v2 + v2_n
    ans2 = v2_1 + v2_v1 + v1_n
    result = min(ans1, ans2)
    if v1 == 1:
        result = v2_1 + v2_n
    if v2 == n:
        result = v1_1 + v1_n
        
    if (result == float('inf')): print(-1)
    else: print(result)