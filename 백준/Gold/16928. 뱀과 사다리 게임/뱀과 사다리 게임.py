import sys
from collections import deque

input = sys.stdin.readline
 
def bfs(board, ladder, snake):
    deq = deque()
    deq.append((1, 0))
    
    while deq:
        loc, cnt = deq.popleft()
        
        if cnt > board[loc]:
            continue
        if loc >= 100:
            continue
        
        for i in range(1, 7):
            nloc = loc + i
            ncnt = cnt + 1
            if nloc in ladder.keys():
                nloc = ladder[nloc]
            if nloc in snake.keys():
                nloc = snake[nloc]
                
            if nloc > 100:
                break
            if board[nloc] < ncnt:
                continue
            
            deq.append((nloc, ncnt))
            board[nloc] = ncnt
    # print(board)
    return board[100]
            
    
if __name__ == "__main__":
    n, m = map(int, input().split())
    board = [float("inf") for i in range(101)]
    
    ladder = dict()
    for i in range(n):
        x, y = map(int, input().split())
        ladder[x] = y
        
    snake = dict()
    for i in range(m):
        x, y = map(int, input().split())
        snake[x] = y
    
    
    print(bfs(board, ladder, snake))
    