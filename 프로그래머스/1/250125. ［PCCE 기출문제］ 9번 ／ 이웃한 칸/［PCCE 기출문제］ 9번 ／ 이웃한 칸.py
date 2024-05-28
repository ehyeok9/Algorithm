def solution(board, h, w):
    dy = [0, 0, -1, 1]
    dx = [1, -1, 0, 0]
    
    answer = 0
    color = board[h][w]
    for i in range(4):
        ny = h + dy[i]
        nx = w + dx[i]
        
        if (ny >= len(board) or ny < 0) or (nx >= len(board[0]) or nx < 0): continue
        if board[ny][nx] == color:
            answer += 1
            
    return answer