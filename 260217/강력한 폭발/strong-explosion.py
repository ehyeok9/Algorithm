import sys

input = sys.stdin.readline

N = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(N)
]

BOMB = 1
dls = [
    [(-1, 0), (-2, 0), (1, 0), (2, 0)]
    , [(-1, 0), (1, 0), (0, -1), (0, 1)]
    , [(-1, -1), (-1, 1), (1, -1), (1, 1)]
]

answer = -1

def inRange(y, x):
    return (0 <= y < N) and (0 <= x < N)

def getArea(locs, selected):
    areas = set(locs)

    for pos, idx in zip(locs, selected):
        cy, cx = pos
        for dy, dx in dls[idx]:
            ny, nx = cy + dy, cx + dx
            if inRange(ny, nx):
                areas.add((ny, nx))
    
    return len(areas)

def backtracking(locs, selected):
    global answer

    if (len(locs) == len(selected)):
        area = getArea(locs, selected)
        # print(selected, area)
        answer = max(answer, area)
        return
    
    for i in range(3):
        selected.append(i)
        backtracking(locs, selected)
        selected.pop()

def simulation():
    # 폭탄 위치 찾기
    locs = []
    for y in range(N):
        for x in range(N):
            if (grid[y][x] == BOMB):
                locs.append((y, x))
    
    # print(locs)
    backtracking(locs, [])

    print(answer)
if __name__=="__main__":
    simulation()