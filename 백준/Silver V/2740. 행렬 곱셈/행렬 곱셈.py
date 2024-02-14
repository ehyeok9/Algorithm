import sys

input = sys.stdin.readline

global n, m, k

def multply(A, B):
    global n, m, k
    result = [[0 for _ in range(k)] for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            for p in range(k):
                result[i][p] += A[i][j] * B[j][p]
    
    for row in result:
        print(*row)

if __name__ == "__main__":
    n,m = map(int, input().split())
    A = []
    for _ in range(n):
        A.append(list(map(int, input().split())))
        
    m, k = map(int, input().split())
    B = []
    for _ in range(m):
        B.append(list(map(int, input().split())))
    
    multply(A,B)