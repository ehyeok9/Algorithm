import sys

input = sys.stdin.readline 

N = int(input())
lines = [
    tuple(map(int, input().split()))
    for _ in range(N)
]
answer = 0

def isOverlap(arr):
    arr.sort()
    
    for i in range(len(arr) - 1):
        cy, cx = arr[i]
        ny, nx = arr[i + 1]
        
        if (cx >= ny):
            return True
        
    return False


def backtracking(idx, selected):
    global answer

    if (len(selected) > N):
        return
    
    if not isOverlap(selected):
        answer = max(answer, len(selected))

    for i in range(idx, N):
        selected.append(lines[i])
        backtracking(i, selected)
        selected.pop()

if __name__=="__main__":
    backtracking(0, [])

    print(answer)