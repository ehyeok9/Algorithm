import sys

input = sys.stdin.readline

global matrix

def divide_conquer(n, y1, y2, x1, x2):
    if (n == 3):
        for i in range(x1, x2):
            matrix[y2][i] = '*'
        matrix[y1+1][x1+1] = '*'
        matrix[y1+1][x1+3] = '*'
        matrix[y1][x1+2] = '*'
        return
    
    divide_conquer(n//2, y1 + n//2, y2, x1, x2 - n)
    divide_conquer(n//2, y1 + n//2, y2, x1 + n, x2)
    divide_conquer(n//2, y1, y2 - n//2, x1 + n//2, x2 - n//2)
    

if __name__ == "__main__":
    N = int(input())
    matrix = [[' ' for _ in range(2*N + 1)] for i in range(N+1)]
    
    divide_conquer(N, 1, N, 1, 2*N)
    
    for i in range(1, N+1):
        print("".join(matrix[i][1:]))        