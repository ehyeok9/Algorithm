import sys
from collections import deque

input = sys.stdin.readline

def dfs(graph, parent, node, visited):
    for vertex in graph[node]:
        if vertex not in visited and parent[vertex] == vertex:
            parent[vertex] = node
            dfs(graph, parent, vertex, visited)

if __name__ == "__main__":
    sys.setrecursionlimit(10**6)
    n = int(input().strip())
    
    graph = {}
    parent = [0]
    for i in range(1,n+1):
        parent.append(i)
        graph[i] = []
    
    for i in range(n-1):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    visited = set()
    dfs(graph, parent, 1, visited)
    
    print(*parent[2:], sep='\n')