import sys

input = sys.stdin.readline

global n

def multiply(a, b):
    result =[[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += (a[i][k] * b[k][j]) % 1000
    
    for i in range(n):
        for j in range(n):
            result[i][j] %= 1000
            
    return result

def modulo(matrix):
    for i in range(n):
        for j in range(n):
            matrix[i][j] %= 1000
            
    return matrix

def recursion(matrix, n):
    if n == 1:
        return modulo(matrix)
    elif n % 2 == 0:
        return recursion(multiply(matrix, matrix), n//2)
    else:
        return multiply(matrix, recursion(multiply(matrix, matrix), (n-1)//2))

if __name__ == "__main__":
    n, B = map(int, input().split())
    
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split())))
        
    answer = recursion(matrix, B)
    
    for i in range(n):
        print(*answer[i])

    