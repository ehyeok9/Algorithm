import sys

input = sys.stdin.readline

global n, m, house, chicken, visited, result

def getDistance(visited):
    totalDistance = 0
    
    for i in range(len(house)):
        y, x = house[i]
        minDistance = float('inf')
        for j in range(len(chicken)):
            if visited[j] == False:
                cy, cx = chicken[j]
                minDistance = min(minDistance, abs(y-cy) + abs(x-cx))
        totalDistance += minDistance
    
    return totalDistance

def backTracking(count, index):
    global result
    
    if count == m:
        result = min(result, getDistance(visited))
        return 
    
    for i in range(index, len(chicken)):
        if visited[i] == False:
            visited[i] = True
            backTracking(count-1, i+1)
            visited[i] = False
    
if __name__ == "__main__":
    n, m = map(int, input().split())
    result = float('inf')
    
    house = []
    chicken = []
    for i in range(n):
        temp = list(map(int, input().split()))
        for j in range(len(temp)):
            if temp[j] == 1:
                house.append((i+1, j+1)) 
            elif temp[j] == 2:
                chicken.append((i+1, j+1))
                
    visited = [False] * len(chicken)
    
    backTracking(len(chicken), 0)
    
    print(result)
    