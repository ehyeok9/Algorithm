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
    
    tree = [[] for i in range(n+1)]
    for i in range(n):
        info = list(map(int, input().split()))
        for j in range(1, len(info)-1, 2):
            tree[info[0]].append((info[j], info[j+1]))
    
    distance = [-1 for i in range(n+1)]
    distance[1]  = 0
    dfs(tree, 1, distance, 0)
    node1 = distance.index(max(distance))
    # print(node1)
    distance = [-1 for i in range(n+1)]
    distance[node1]  = 0
    dfs(tree, node1, distance, 0)
    print(max(distance))
    