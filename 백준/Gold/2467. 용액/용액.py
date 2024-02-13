import sys

input = sys.stdin.readline

global n, solution
global sumation, p1, p2

def search(start, end):
    global sumation, p1, p2
    if (start >= end):
        return 
    
    temp = solution[start] + solution[end]
    
    if abs(temp) <= abs(sumation):
        sumation = temp
        p1, p2 = solution[start], solution[end]
    
    if -temp > temp:
        search(start+1, end)
    else:
        search(start, end-1)
            

if __name__ == "__main__":
    n = int(input())
    solution = list(map(int, input().split()))
    sys.setrecursionlimit(10 ** 6)
    solution.sort()
    sumation = float("inf")
    p1, p2 = -1, -1
    
    search(0, n-1)
    
    print(p1, p2)
    