answer = 0

def backtracking(number, visited, selected, idx):
    global answer
    if len(selected) == 3:
        if sum(selected) == 0:
            answer += 1
        return
    
    for i in range(idx, len(number)):
        if visited[i] == False:
            visited[i] = True
            selected.append(number[i])
            backtracking(number, visited, selected, i)
            selected.pop()
            visited[i] = False
            
            
def solution(number):
    # global answer
    visited = [False for _ in range(len(number))]
    
    backtracking(number, visited, [], 0)
    
    return answer