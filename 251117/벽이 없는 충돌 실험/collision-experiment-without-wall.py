import sys
from collections import deque

input = sys.stdin.readline

def simulation(N, beads):
    # board를 2N으로 만들기
    board = [
        [[] for _ in range(3 * N + 2)]
        for _ in range(3 * N + 2)
    ]

    preprocessedBeads = []
    # 구슬의 좌표를 좌표평면이 아닌 배열 형식으로 재구성 -> 걍 r, c에 N다 동일하게 더해버리면 되잖아. 메모리 더 써
    # 범위 0.5N에서 1.5N임. * 2 해주면 N ~ 3N까지가 보드의 좌표임 -> 짝수일경우 기준을 잘 모르겠네 -> +- 2 로 한 칸씩 더 늘려주자
    # 총 범위 = (N - 2) ~ (3N + 2)
    for x, y, w, d, num in beads:
        preprocessedBeads.append([-int(y) * 2 + N, int(x) * 2 + N, int(w), d, num])

    MIN_BORDER = N - 2
    MAX_BORDER = 3 * N + 2

    deq = deque(preprocessedBeads)
    lastCrushTime = -1

    # 처음 좌에서 우로 가는데 2N * 2
    for t in range(1, 4 * N + 1):
        
        # 반칸 옮기기
        while deq:
            r, c, w, d, num = deq.popleft()
            nr, nc = oneStep(r, c, d)
            # print(t, nr, nc, num)

            # 범위 넘어간 건 그냥 무시
            if (nr < MIN_BORDER or nc < MIN_BORDER or nr >= MAX_BORDER or nc >= MAX_BORDER):
                continue
            
            board[nr][nc].append([w, d, num])
        
        # printBoard(board)

        # 충돌 처리하기
        for y in range(MIN_BORDER, MAX_BORDER):
            for x in range(MIN_BORDER, MAX_BORDER):
                # if (len(board[y][x]) >= 1):
                #     print(y, x, board[y][x])
                if (len(board[y][x]) > 1):
                    board[y][x].sort(key = lambda z: (-z[0], -z[2]))
                    board[y][x] = [board[y][x][0]]
                    lastCrushTime = t
        
        # 남은 것들은 다시 deque에 넣고 board 초기화
        for r in range(MIN_BORDER, MAX_BORDER):
            for c in range(MIN_BORDER, MAX_BORDER):
                for w, d, num in board[r][c]:
                    deq.append([r, c, w, d, num])
                board[r][c] = []

    print(lastCrushTime)

def oneStep(r, c, d):
    if ('L' == d):
        return r, c - 1
    elif ('R' == d):
        return r, c + 1
    elif ('U' == d):
        return r - 1, c
    elif ('D' == d):
        return r + 1, c

def printBoard(board):
    for line in board:
        print(*line)   



if __name__=="__main__":
    T = int(input())
    for _ in range(T):
        N = int(input())
        beads = [
            list(input().strip().split()) + [i+1]
            for i in range(N)
        ]

        simulation(N, beads)


    