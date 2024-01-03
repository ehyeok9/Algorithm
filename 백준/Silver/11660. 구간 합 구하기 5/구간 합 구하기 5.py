import sys

input = sys.stdin.readline

def getSum(arr, n):
    prefixSum = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,n+1):
            prefixSum[i][j] = arr[i-1][j-1] + prefixSum[i-1][j] + prefixSum[i][j-1] - prefixSum[i-1][j-1]
    return prefixSum            

if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    
    prefixSum = getSum(arr, n)
    for _ in range(m):
        x1, y1, x2, y2 = map(int, input().split())
        answer = prefixSum[x2][y2] - prefixSum[x2][y1-1] - prefixSum[x1-1][y2] + prefixSum[x1-1][y1-1]
        print(answer)