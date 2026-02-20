import sys

input = sys.stdin.readline

N, M = map(int, input().split())
lines = [
    list(map(int, input().split()))
    for _ in range(M)
]
initialResult = []
answer = M

def dfs(node, depth, graph, maxDepth):
    if (depth > maxDepth):
        return node
    
    # 가로줄의 선이 있는 경우
    if (depth in graph):
        
        # 가로줄이 겹쳐 주어지는 경우는 없기에 좌/우만 검사
        # 오른쪽 가로줄이 있다 (node가 N일 때 어차피 N + 1에 대한 가로줄은 입력으로 안 주어지기에 if문 조건 패스)
        if (node in graph[depth]):
            return dfs(node + 1, depth + 1, graph, maxDepth)
        # 왼쪽 가로줄이 있다 (node가 1일 때 어차피 0에 대한 가로줄은 입력으로 안 주어지기에 if문 조건 패스)
        elif ((node - 1) in graph[depth]):
            return dfs(node - 1, depth + 1, graph, maxDepth)
        # 둘 다 없다
        else:
            return dfs(node, depth + 1, graph, maxDepth)
    else:
        # 가로줄 선이 없으면 바로 내려간다
        return dfs(node, depth + 1, graph, maxDepth)

def backtracking(start, path, R):
    global answer, initialResult

    if (len(path) == R):
        selected = []
        for i in range(M):
            if ((i + 1) in path):
                selected.append(True)
            else:
                selected.append(False)
        
        result = processing(selected)
        # print(R, answer, result, initialResult)
        if (result == initialResult) and (R < answer):
            answer = R

        return
    
    for i in range(start, M + 1):
        path.append(i)
        backtracking(i + 1, path, R)
        path.pop()

def processing(selected):
    # 가로줄 순서별로 어떻게 연결되어 있는지 그래프로 만들기
    graph = {}
    maxDepth = 0
    for i in range(M):
        if (selected[i]):
            a, b = lines[i]
            maxDepth = max(maxDepth, b)
            graph.setdefault(b, dict())[a] = a + 1
    
    result = []
    for i in range(1, N + 1):
        result.append(dfs(i, 1, graph, maxDepth))

    return result

def simulation():
    global answer, initialResult

    # 처음 사다리 탔을 때 결과값 찾기
    selected = [True for _ in range(M)]
    initialResult = processing(selected)
    
    # 조합으로 선택된 가로줄별 결과 구하기
    for i in range(0, M + 1):
        backtracking(1, [], i)

    print(answer)
    

if __name__=="__main__":
    simulation()

