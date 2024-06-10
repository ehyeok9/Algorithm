from collections import deque

dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]

def solution(land):
    global lenY, lenX
    
    lenY = len(land)
    lenX = len(land[0])
    answer = [0 for _ in range(lenX)]
    visited = [[False for _ in range(lenX)] for _ in range(lenY)]
    
    for y in range(lenY):
        for x in range(lenX):
            if land[y][x] == 1 and visited[y][x] == False :
                bfs(land, (y,x), visited, answer)
        
    return max(answer)

def bfs(land, point, visited, answer):
    deq = deque([point])
    count = 1
    visited[point[0]][point[1]] = True
    xList = set([point[1]])
    
    while deq:
        y, x = deq.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if (ny >= lenY or ny < 0) or (nx >= lenX or nx < 0): continue
            if (land[ny][nx] == 0 or visited[ny][nx] == True): continue
            count += 1
            visited[ny][nx] = True
            deq.append([ny,nx])
            xList.add(nx)
        
    for x in list(xList):
        answer[x] += count
    
        
        
    