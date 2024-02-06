import sys

input = sys.stdin.readline

global V, E, edges
global parent

def getParent(node):
    if parent[node] == node:
        return node
    parent[node] = getParent(parent[node])
    return parent[node]

def union(A, B):
    a = getParent(A)
    b = getParent(B)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def isConnected(A, B):
    a = getParent(A)
    b = getParent(B)
    
    if (a == b):
        return True
    return False

def kruskal():
    result = 0
    
    for C, edge in edges:
        A, B = edge
        if (isConnected(A,B)): continue
        result += C
        union(A,B)
        # print(A,B,C)

    return result
        
    

if __name__ == "__main__":
    V, E = map(int, input().split())
    
    edges = []    
    for _ in range(E):
        A, B, C = list(map(int, input().split()))
        edges.append([C, [A, B]])
    edges.sort()
    
    parent = [ x for x in range(V+1) ]
    
    result = kruskal()
    
    print(result)
            