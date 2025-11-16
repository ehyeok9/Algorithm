import sys
from collections import deque

input = sys.stdin.readline

N, M, T, K = map(int, input().split())
board = [
    [[] for _ in range(N)]
    for _ in range(N)
]
commands = [
    list(input().strip().split()) + [i + 1]
    for i in range(M)
]

def simulation():
    # int 및 위치 -1로 전처리
    preprocessedCommands = []
    for r, c, d, v, num in commands:
        preprocessedCommands.append([int(r) - 1, int(c) -1, d, int(v), num])

    deq = deque(preprocessedCommands)
    
    for t in range(T):  
        # 공 하나씩 움직이기
        while deq:
            r, c, d, v, num = deq.popleft()
            nr, nc, nd = moveBead(r, c, d, v)
            
            board[nr][nc].append([nd, v, num])
        
        # 보드판 돌면서 충돌 검출하기
        for y in range(N):
            for x in range(N):
                if (len(board[y][x]) > K):
                    removeLowerPriorityBead(y, x)
        
        # 남은 구슬은 다시 deque에 담기
        for r in range(N):
            for c in range(N):
                for d, v, num in board[r][c]:
                    deq.append([r, c, d, v, num])
                
                # board 초기화
                board[r][c] = []
    
    # 다 끝나고 남은 구슬
    print(len(deq))

def printBoard():
    for line in board:
        print(*line)
                
def removeLowerPriorityBead(y, x):
    # v, num 로 내림차순 정렬
    board[y][x].sort(key = lambda x: (-x[1], -x[2]))
    # 삭제
    board[y][x] = board[y][x][:K]

def moveBead(r, c, d, v):
    for i in range(v):
        nr, nc = oneStep(r, c, d)
        nd = d

        if (nr < 0 or nr >= N or nc < 0 or nc >= N):
            nd = chagneDirection(d)
            nr, nc = oneStep(r, c, nd)
        
        r, c, d = nr, nc, nd

    return r, c, d
        

def oneStep(r, c, d):
    if ('L' == d):
        return r, c - 1
    elif ('R' == d):
        return r, c + 1
    elif ('U' == d):
        return r - 1, c
    elif ('D' == d):
        return r + 1, c

def chagneDirection(d):
    if ('L' == d):
        return 'R'
    elif ('R' == d):
        return 'L'
    elif ('U' == d):
        return 'D'
    elif ('D' == d):
        return 'U'

if __name__=="__main__":
    simulation()