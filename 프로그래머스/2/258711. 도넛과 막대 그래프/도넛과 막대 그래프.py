from collections import deque

def solution(edges):    
    # 인접리스트로 변경
    edgeGraph = dict()
    for edge in edges:
        start, end = edge
        if start in edgeGraph:
            edgeGraph[start].append(end)
        else:
            edgeGraph[start] = [end]
    
    # 사이클 노드 찾기
    cycleNode = findCycleNode(edgeGraph)
    
    answer = [cycleNode, 0, 0, 0]
    visited = [False for _ in range(maxNodeNum+1)]
    
    # bfs로 그래프 형태 찾기
    nodes = edgeGraph[cycleNode]
    for node in nodes:
        bfs(edgeGraph, visited, answer, node)
        
    return answer

def bfs(edges, visited, answer, node):
    deq = deque([node])
    visited[node] = True
    edgeCount = 0
    vertexCount = 0
    
    while deq:
        cur = deq.popleft()
        vertexCount += 1
        if cur not in edges: continue
        edgeCount += len(edges[cur])
        
        for nxt in edges[cur]:
            if visited[nxt] == True: continue
            deq.append(nxt)
            visited[nxt] = True
    
    if edgeCount < vertexCount:
        answer[2] += 1
    elif edgeCount > vertexCount:
        answer[3] += 1
    else:
        answer[1] += 1

def findCycleNode(edges):
    global maxNodeNum
    
    # 나가는 방향이 있고 -> keys에 있다, 들어오는 방향이 없는 것 -> value에 없다.
    nodes = set(edges.keys())
    values = set()
    
    for val in edges.values():
        values.update(val)
    
    candidate = list(nodes - values)
    maxNodeNum = max(list(nodes | values))
    
    # cycle 노드는 최소 2개의 edge를 가진다.
    step1 = []
    for node in candidate:
        if len(edges[node]) >= 2:
            step1.append(node)
            
    if len(step1) == 1:
        return step1[0]
    
    # cycle 노드는 전체 노드를 순회할 수 있어야 한다.
    for node in step1:
        visited = [False for _ in range(maxNodeNum + 1)]
        visited[node] = True
        dfs(edges, node, visited)
        if sum(visited) == maxNodeNum:
            return node
        
    return step1[0]

def dfs(edges, curNode, visited):
    if curNode not in edges:
        return
    
    for nxtNode in edges[curNode]:
        if visited[nxtNode] == False:
            visited[nxtNode] = True
            dfs(edges, nxtNode, visited)
    