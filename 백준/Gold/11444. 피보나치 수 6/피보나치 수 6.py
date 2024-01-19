import sys
import heapq

input = sys.stdin.readline

def multiply(a,b):
    result = [[0,0], [0,0]]
    
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += (a[i][k] * b[k][j]) % 1000000007
    
    for i in range(2):
        for j in range(2):
            result[i][j] %=1000000007
                
    return result

def fibo(n):
    if (n < 0): return [[0,0],[0,0]]
    elif (n <= 1): return [[1,1],[1,0]]
    elif (n%2 == 1):
        return multiply(fibo(n-1), [[1,1],[1,0]])
    else:
        matrix = fibo(n//2)
        return multiply(matrix, matrix)

if __name__ == "__main__":
    n = int(input())
        
    print(fibo(n)[0][1])