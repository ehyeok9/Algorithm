def solution(park, routes):
    answer = []
    H, W = len(park), len(park[0])
    start = None
    
    for i in range(H):
        for j in range(W):
            if park[i][j] == "S":
                start = (i,j)
                
    ny, nx = start
    for command in routes:
        direction, distance = command.split()
        distance = int(distance)
        ny, nx = check(park, [ny, nx], direction, distance, H, W)
    
    return [ny, nx]

def check(park, start, direction, distance, H, W):
    y, x = start
    if direction == "N":
        for i in range(1, distance+1):
            if not (0 <= y - i < H): return start
            if park[y - i][x] == "X": return start
        y -= distance
    if direction == "S":
        for i in range(1, distance+1 ):
            if not (0 <= y + i < H): return start
            if park[y + i][x] == "X": return start
        y += distance
    if direction == "E":
        for i in range(1,distance+1):
            if not (0 <= x + i < W): return start
            if park[y][x+i] == "X": return start
        x += distance
    if direction == "W":
        for i in range(1, distance+1):
            if not (0 <= x - i < W): return start
            if park[y][x-i] == "X": return start
        x -= distance
    return y,x
    
    