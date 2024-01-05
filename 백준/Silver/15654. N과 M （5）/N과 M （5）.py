import sys

input = sys.stdin.readline


def backtracking(arr, n, m, visited, answer):
    if len(visited) == m:
        answer.append(visited[:])
        return
    
    for i in range(n):
        if arr[i] not in visited:
            visited.append(arr[i])
            backtracking(arr, n, m, visited, answer)
            visited.pop()

if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    answer = []
    backtracking(arr, n, m, [], answer)
    # answer.sort()
    
    for lit in answer:
        print(*lit)
    
    
    
    
    
    
    