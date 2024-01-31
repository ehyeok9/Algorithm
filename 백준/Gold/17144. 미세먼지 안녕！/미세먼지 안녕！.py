import sys

input = sys.stdin.readline

global R, C, T
global matrix, move
global upAir, downAir

dy = [0, 0, -1, 1]
dx = [-1, 1, 0,0 ]

def spread():
    for i in range(R):
        for j in range(C):
            move[i][j] =  matrix[i][j] // 5
    
    for y in range(R):
        for x in range(C):
            if matrix[y][x] == -1: continue
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if not (0 <= ny < R and 0 <= nx < C): continue
                if matrix[ny][nx] != -1:
                    matrix[y][x] -= move[y][x]
                    matrix[ny][nx] += move[y][x]
    

def clean():
    upStart = upAir - 1
    for i in range(upStart, 0, -1):
        matrix[i][0] = matrix[i-1][0]
    for i in range(C-1):
        matrix[0][i] = matrix[0][i+1]
    for i in range(0, upAir):
        matrix[i][C-1] = matrix[i+1][C-1]
    for i in range(C-1, 1, -1):
        matrix[upAir][i] = matrix[upAir][i-1]
    matrix[upAir][1] = 0
    
    downStart = downAir + 1
    for i in range(downStart, R-1):
        matrix[i][0] = matrix[i+1][0]
    for i in range(C-1):
        matrix[R-1][i] = matrix[R-1][i+1]
    for i in range(R-1, downAir, -1):
        matrix[i][C-1] = matrix[i-1][C-1]
    for i in range(C-1, 1,-1):
        matrix[downAir][i] = matrix[downAir][i-1]
    matrix[downAir][1] = 0


    
if __name__ == "__main__":
    R, C, T = map(int, input().split())
    
    matrix = []
    for _ in range(R):
        matrix.append(list(map(int, input().split())))
    
    upAir, downAir = 0, 0
    for i in range(R):
        if matrix[i][0] == -1:
            upAir = i
            downAir = i + 1
            break
    
    move = [[0] * C for _ in range(R)]
    for i in range(T):
        spread()
        clean()
        
    print(sum(map(sum, matrix)) + 2)