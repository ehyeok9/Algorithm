import sys

input = sys.stdin.readline

def getSum(arr, n):
    prefixSum = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,n+1):
            prefixSum[i][j] = arr[i-1][j-1] + prefixSum[i-1][j] + prefixSum[i][j-1] - prefixSum[i-1][j-1]
    return prefixSum   

def getOneDimensionSum(arr, n, m):
    sumation = [0]         
    moduler = dict()
    count = 0
    
    for i in range(n):
        temp = sumation[i] + arr[i]
        sumation.append(temp)
        mod = temp % m
        if (mod == 0):
            count += 1
        if  mod not in moduler.keys():
            moduler[mod] = 1
        else:
            moduler[mod] += 1    

    return moduler, count
        
if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    
    moduler, answer = getOneDimensionSum(arr, n, m)
    
    for key in moduler.keys():
        answer += (moduler[key] * (moduler[key]-1)) // 2
    
    print(answer)
    
    