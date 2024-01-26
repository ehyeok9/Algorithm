import sys
import heapq

input = sys.stdin.readline

global n, m, r, items, graph

def getTotal(distance):
    result = 0
    for i in range(1, n+1):
        if distance[i] <= m:
            result += items[i]
    return result

def dijkstra(start):
    distance = [float('inf')] * (n+1)
    distance[start] = 0
    heap = []
    heapq.heappush(heap, (0, start))
    
    while heap:
        dist, node = heapq.heappop(heap)
        
        if dist > m: continue
        
        for nxt, cost in graph[node]:
            if dist + cost <= m:
                distance[nxt] = min(distance[nxt], dist + cost)
                heapq.heappush(heap, (distance[nxt], nxt))
                
    return getTotal(distance)

def floydWarshall():
    distance = [[float("inf") for _ in range(n+1)] for _ in range(n+1)]
    # print(distance)
    for _ in range(r):
        a, b, l = map(int, input().split())
        distance[a][b] = l
        distance[b][a] = l
    
    for i in range(1, n+1):
        distance[i][i] = 0
    
    for k in range(1, n+1):
        for i in range(1, n+1):
            if distance[i][k] > m: continue
            for j in range(1,n+1):
                if (distance[i][k] + distance[k][j]) > m : continue
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    maxVal = 0
    # print(distance)
    for i in range(1, n+1):
        maxVal = max(maxVal, getTotal(distance[i]))
    print(maxVal)
    
    
if __name__ == "__main__":
    n, m, r = map(int, input().split())
    
    items = list(map(int, input().split()))
    items.insert(0, 0)
    
    floydWarshall()