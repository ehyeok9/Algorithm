import sys

input = sys.stdin.readline

def backtracking(arr, n, m, values, visited, start):
    if len(values) == m:
        print(*values)
        return
    
    memo = 0
    for i in range(n):
        if visited[i] == False and memo != arr[i]:
            visited[i] = True
            values.append(arr[i])
            memo = arr[i]
            backtracking(arr, n, m, values, visited, i+1)
            values.pop()
            visited[i] = False

if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    visited = [False for _ in range(n)]
    duplicated = []
    backtracking(arr, n, m, [], visited, 0)
    
    
    
    
    
    
    