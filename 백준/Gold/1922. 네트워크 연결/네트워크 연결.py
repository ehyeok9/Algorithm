import sys
import heapq

input = sys.stdin.readline

global N, M
global edges, parent

def find(node):
    if parent[node] == node:
        return node
    parent[node] = find(parent[node])
    return parent[node]

def isConnected(A,B):
    a = find(A)
    b = find(B)
    
    if a == b:
        return True
    return False 

def union(A,B):
    a = find(A)
    b = find(B)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def kruskal():
    result = 0
    
    while edges:
        cost, edge = heapq.heappop(edges)
        a,b = edge
        
        if (isConnected(a,b)): continue
        result += cost
        union(a,b)
        
    print(result)
    
if __name__ == "__main__":
    N = int(input())
    M = int(input())
    
    edges = []
    for _ in range(M):
        a,b,c = map(int, input().split())
        if (a == b): continue
        heapq.heappush(edges, [c, [a,b]])
    
    parent = [x for x in range(N+1)]
    
    kruskal()
    
    