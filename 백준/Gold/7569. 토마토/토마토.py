import sys
from collections import deque

input = sys.stdin.readline

dh = [0, 0, 0, 0, 1, -1]
dy = [0, 0, 1, -1, 0, 0]
dx = [1, -1, 0, 0, 0, 0]

def getDeque(box):
    deq = deque()
    unfilled = 0
    for i in range(len(box)):
        for j in range(len(box[i])):
            for k in range(len(box[i][j])):
                if box[i][j][k] == 1:
                    deq.append((i, j, k))
                if box[i][j][k] == 0:
                    unfilled += 1
    return deq, unfilled

def getNext(box, deq):
    filled = 0
    new_deq = deque()
    
    while deq:
        h, y, x = deq.popleft()
        for i in range(6):
            nh = h + dh[i]
            ny = y + dy[i]
            nx = x + dx[i]
            if (0 <= nh < len(box)) and (0 <= ny < len(box[nh])) and (0 <= nx < len(box[nh][ny])):
                if box[nh][ny][nx] == 0:
                    box[nh][ny][nx] = 1
                    new_deq.append((nh, ny, nx))
                    filled += 1
    return new_deq, filled

def fillBox(box, deq, unfilled):
    day = 0
    while True:
        deq, filled = getNext(box, deq)
        day += 1
        unfilled -= filled
        if unfilled == 0:
            return day
        if filled == 0:
            return -1    
    

if __name__ == "__main__":
    m, n, h = map(int, input().split())
    
    box = []
    for i in range(h):
        stair = []
        for j in range(n):
            stair.append(list(map(int, input().split())))
        box.append(stair)

    deq, unfilled = getDeque(box)
    if (unfilled == 0):
        print(0)
    else:
        print(fillBox(box, deq, unfilled))