import sys
from collections import deque
import heapq

input = sys.stdin.readline

global N, matrix
global weight, curW

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

def findStart():
    start = []
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 9:
                start = [i,j]
    return start

def bfs(start):
    deq = deque()
    deq.append([start, 0])
    visited = [[False for _ in range(N)] for _ in range(N)]
    visited[start[0]][start[1]] = True
    heap = []
    
    while deq:
        curLoc, time = deq.popleft()
        y,x = curLoc
        
        if 0< matrix[y][x] < curW and matrix[y][x] != 9:
            heapq.heappush(heap, [time, curLoc])
            continue            
        
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if not (0 <= ny < N and 0 <= nx < N): continue
            if matrix[ny][nx] > curW: continue
            if visited[ny][nx]: continue
            deq.append([(ny,nx), time + 1])
            visited[ny][nx] = True
    
    return heap

def getNext(heap):
    topTime, loc = heapq.heappop(heap)
    temp = [loc]
    
    while heap:
        tempTime, loc = heapq.heappop(heap)
        if topTime == tempTime:
            temp.append(loc)
    
    temp.sort(key=lambda x : (x[0], x[1]))
    
    return temp[0], topTime
    

if __name__ == "__main__":
    N = int(input())
    matrix = []
    for _ in range(N):
        matrix.append(list(map(int, input().split())))
    
    start = findStart()
    weight = 0
    curW = 2
    result = 0
    
    while True:
        heap = bfs(start)
        if heap == []:
            break
        
        loc, time = getNext(heap)
        y,x = loc
        
        result += time
        weight += 1
        if weight == curW:
            weight = 0
            curW += 1
            
        matrix[start[0]][start[1]] = 0
        matrix[y][x] = 9
        start = loc
        # print(loc, result, curW, weight)
        
        
        
    print(result)
        
