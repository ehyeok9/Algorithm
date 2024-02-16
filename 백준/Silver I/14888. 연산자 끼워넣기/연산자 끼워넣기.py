import sys

input = sys.stdin.readline

global numbers, operators, N, visited
global maxi, mini

def backtracking(ops):
    global numbers, operator, N, visited
    global maxi, mini
    
    if len(ops) == N-1:
        temp = getResult(ops, numbers)
        maxi = max(maxi, temp)
        mini = min(mini, temp)
        return 

    for i in range(N-1):
        if visited[i] == False:
            ops.append(operators[i])
            visited[i] = True
            backtracking(ops)
            visited[i] = False
            ops.pop()

def getResult(ops, numbers):
    result = numbers[0]
    
    for i in range(1,N):
        result = calc(ops[i-1], result, numbers[i])
        
    return result    

def calc(op, n1, n2):
    if op == 0:
        return n1 + n2
    elif op == 1:
        return n1 - n2
    elif op == 2:
        return n1 * n2
    elif op == 3:
        if n1 < 0:
            return -(-n1 // n2)
        return n1 // n2
    
    
def getOperators(operator):
    result = []
    
    for i in range(4):
        while operator[i] > 0:
            result.append(i)
            operator[i] -= 1
            
    return result

        
if __name__ == "__main__":
    N = int(input())
    numbers = list(map(int, input().split()))
    operator = list(map(int, input().split()))
    
    operators = getOperators(operator)
    visited = [False for _ in range(N-1)]
    
    maxi, mini = -float("inf"), float("inf") 
    backtracking([])
    
    print(maxi)
    print(mini)
    