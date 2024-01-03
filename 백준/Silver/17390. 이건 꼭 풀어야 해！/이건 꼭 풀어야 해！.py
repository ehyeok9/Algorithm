import sys

input = sys.stdin.readline

def getSum(arr, n):
    prefixSum = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,n+1):
            prefixSum[i][j] = arr[i-1][j-1] + prefixSum[i-1][j] + prefixSum[i][j-1] - prefixSum[i-1][j-1]
    return prefixSum   

def getOneDimensionSum(arr, n):
    sumation = [0]         
    for i in range(n):
        sumation.append(sumation[i] + arr[i])
    return sumation

def mergeSort(arr):
    if (len(arr) > 1):
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        
        mergeSort(left)
        mergeSort(right)

        merge(arr, left, right)

def merge(arr, left, right):
    i = j = k = 0
    
    while (i < len(left) and j < len(right)):
        if (left[i] < right[j]):
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j] 
            j += 1
        k += 1

    while (i < len(left)):
        arr[k] = left[i]
        i += 1
        k += 1
        
    while (j < len(right)):
        arr[k] = right[j]
        j += 1
        k += 1

        
if __name__ == "__main__":
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))
    mergeSort(arr)
    sumation = getOneDimensionSum(arr, n)
    for _ in range(q):
        L, R = map(int, input().split())
        print(sumation[R] - sumation[L-1])