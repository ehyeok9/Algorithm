import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(tree, node, distance, weight):
    for item in tree[node]:
        vertex, value = item
        if distance[vertex] == -1:
            distance[vertex] = distance[node] + value
            dfs(tree, vertex, distance, weight + value)
    
if __name__ == "__main__":
    n = int(input())
    tree = dict()
    max_weight = 0
    
    if n == 1:
        print(0)
        exit()
        
    for _ in range(n-1):
        parent, child, weight = map(int, input().split())
        tree[parent] = tree.get(parent, []) + [(child, weight)]
        tree[child] = tree.get(child, []) + [(parent, weight)]
    
    visited = []
    distance = [-1 for _ in range(n+1)]
    distance[1] = 0
    dfs(tree, 1, distance, 0)
    
    # print(distance.index(max(distance)))
    node1 = distance.index(max(distance))
    distance = [-1 for _ in range(n+1)]
    distance[node1] = 0
    dfs(tree, node1, distance, 0)
    
    print(max(distance))