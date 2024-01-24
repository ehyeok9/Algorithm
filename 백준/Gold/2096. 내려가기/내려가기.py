import sys

input = sys.stdin.readline
    
if __name__ == "__main__":
    n = int(input())

    prevMax, curMax, postMax = 0, 0, 0
    prevMin, curMin, postMin = 0, 0, 0
    
    for _ in range(n):
        pos0, pos1, pos2 = map(int, input().split())
    
        prevTemp, curTemp, postTemp = prevMax, curMax, postMax
        prevMax = max(prevTemp, curTemp) + pos0
        curMax = max(prevTemp, curTemp, postTemp) + pos1
        postMax = max(curTemp, postTemp) + pos2
        
        prevTemp, curTemp, postTemp = prevMin, curMin, postMin
        prevMin = min(prevTemp, curTemp) + pos0
        curMin = min(prevTemp, curTemp, postTemp) + pos1
        postMin = min(curTemp, postTemp) + pos2
    
    print(max(prevMax, curMax, postMax), min(prevMin, curMin, postMin))
    
        
    
    