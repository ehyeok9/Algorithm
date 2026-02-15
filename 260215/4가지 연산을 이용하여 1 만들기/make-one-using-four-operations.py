import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
visited = [-1 for num in range(1, 1000001)]

def inRange(num):
    return (0 <= num < 1000001)

def bfs():
    deq = deque([N])
    visited[N] = 0

    while deq:
        
        curNum = deq.popleft()

        if (curNum == 1):
            return visited[1]

        minusNum = curNum - 1
        if inRange(minusNum) and (visited[minusNum] == -1):
            visited[minusNum] = visited[curNum] + 1
            deq.append(minusNum)
        
        plusNum = curNum + 1
        if inRange(plusNum) and (visited[plusNum] == -1):
            visited[plusNum] = visited[curNum] + 1
            deq.append(plusNum)
        
        if (curNum % 2 == 0):
            divideNum = curNum // 2
            if inRange(divideNum) and (visited[divideNum] == -1):
                visited[divideNum] = visited[curNum] + 1
                deq.append(divideNum)
        
        if (curNum % 3 == 0):
            divideNum = curNum // 3
            if inRange(divideNum) and (visited[divideNum] == -1):
                visited[divideNum] = visited[curNum] + 1
                deq.append(divideNum)



if __name__=="__main__":
    print(bfs())