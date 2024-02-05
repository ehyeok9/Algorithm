import sys

input = sys.stdin.readline

global N, M, arr
global visited

def backTracking(count, num):
    if len(count) == M:
        print(*count)
        return
    
    for i in range(num, N):
        count.append(arr[i])
        backTracking(count, i)
        count.pop()

if __name__ == "__main__":
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    arr = list(set(arr))
    arr.sort()
    N = len(arr)
    
    backTracking([], 0)