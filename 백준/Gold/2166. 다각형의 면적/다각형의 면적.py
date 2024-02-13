import sys

input = sys.stdin.readline

def triangleArea(points, n):
    area = 0
    for i in range(n):
        area += points[i][0] * points[i+1][1]
        area -= points[i+1][0] * points[i][1]
    
    return abs(area)/2

if __name__ == "__main__":
    n = int(input())
    
    points = []
    
    for _ in range(n):
        x, y = map(int, input().split())
        points.append((x,y))
    
    points.append(points[0])
    result = triangleArea(points, n)
    
    print(result)
        
        
    