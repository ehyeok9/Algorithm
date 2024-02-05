import sys

input = sys.stdin.readline

global N, arr

def dynamicProgramming():
    # memo = [[0]*i for i in range(1,N+1)]
    # for i in range(N):
    #     memo[i][0] = 1
    
    memo = [[1,0] for _ in range(N)] 
    for i in range(N):
        for j in range(i):
            if arr[i] > arr[j]:
                memo[i][0] = max(memo[i][0], memo[j][0]+1)
            
    for i in range(N, -1, -1):
        for j in range(N-1, i, -1):
            if arr[i] > arr[j]:
                memo[i][1] = max(memo[i][1], memo[j][1]+1)
    
    result = 0
    for val in memo:
        result = max(result, sum(val))
        
    print(result)
        

if __name__ == "__main__":
    N = int(input())
    arr = list(map(int, input().split()))
    
    dynamicProgramming()