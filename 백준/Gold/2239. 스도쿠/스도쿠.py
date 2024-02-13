import sys

input = sys.stdin.readline

def check(y, x, value):
    for i in range(9):
        if board[y][i] == value or board[i][x] == value:
            return False
        
    start_y, start_x = 3 * (y // 3), 3 * (x // 3)
    for i in range(3):
        for j in range(3):
            if board[start_y + i][start_x + j] == value:
                return False
    return True

def checkBoard():
    for i in range(9):
        if "0" in board[i]:
            return False
    return True

def fillBoard(y, x):
    if y == 9:
        if checkBoard():
            for line in board:
                print("".join(line))
            sys.exit()
        return

    if board[y][x] == '0':
        for j in range(len(fillNum[y])):
            if visited[y][j] == False and check(y, x, fillNum[y][j]):
                board[y][x] = fillNum[y][j]
                visited[y][j] = True
                if x == 8:
                    fillBoard(y + 1, 0)
                else:
                    fillBoard(y, x + 1)
                visited[y][j] = False
                board[y][x] = "0"
    else:
        if x == 8:
            fillBoard(y + 1, 0)
        else:
            fillBoard(y, x + 1)

if __name__ == "__main__":
    board = []
    
    fillNum = []
    number = set([str(i) for i in range(1,10)])
    
    for i in range(9):
        board.append(list(input().strip()))
        fillNum.append(sorted(list(number -  set(board[i]))))
    
    visited = [[False for _ in range(len(fillNum[i]))] for i in range(9)]
    fillBoard(0, 0)
