import sys

input = sys.stdin.readline

def dfs(graph, visited, node, answer):
    if (node not in graph.keys()):
        return answer
        
    nxt = graph[node]
    
    if (nxt is None or nxt == []):
        return answer
    
    for nxtNode in nxt:
        if not visited[nxtNode]:
            visited[nxtNode] = True
            answer = dfs(graph, visited, nxtNode, answer + 1)

    return answer

if __name__=="__main__":
    N, M = map(int, input().split())
    graph = {}
    visited = [False for _ in range(N + 1)]
    for _ in range(M):
        x, y = map(int, input().split())
        graph.setdefault(x, []).append(y)
        graph.setdefault(y, []).append(x)
    
    visited[1] = True
    print(dfs(graph, visited, 1, 0))
    