import sys

input = sys.stdin.readline

def floyd_warshall(graph, n):
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1): 
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    

if __name__ == "__main__":
    n = int(input())
    m = int(input())
    
    graph = [[float('inf') for j in range(n+1)] for i in range(n+1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a][b] = min(graph[a][b], c)
        
    for s in range(1, n+1):
        graph[s][s] = 0
    
    floyd_warshall(graph, n)
    
    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i][j] == float('inf'):
                print(0, end=' ')
            else:
                print(graph[i][j], end=' ')
        print()
    
    
    
        