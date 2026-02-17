import sys

input = sys.stdin.readline 

N = int(input())
lines = [
    tuple(map(int, input().split()))
    for _ in range(N)
]
answer = 0

def isOverlap(arr):
    arr = sorted(arr)
    
    for i in range(len(arr) - 1):
        cy, cx = arr[i]
        ny, nx = arr[i + 1]
        
        if (cx >= ny):
            return True
        
    return False


def backtracking(idx, selected):
    global answer, N

    if not isOverlap(selected):
        answer = max(answer, len(selected))

    for i in range(idx, N):
        selected.append(lines[i])
        backtracking(i + 1, selected)
        selected.pop()

if __name__=="__main__":
    backtracking(0, [])

    print(answer)