import sys
from collections import deque

input = sys.stdin.readline

global gears

def printGears():
    for gear in gears:
        print(gear)
    print()
    
def operation(n, d):
    # printGears()
    relation = [[False for i in range(5)] for _ in range(5)]
    for i in range(1,4):
        if gears[i][2] != gears[i+1][6]:
            relation[i][i+1] = True
            relation[i+1][i] = True
    # for rel in relation:
    #     print(*rel[1:])
    # print()
    
    deq = deque()
    deq.append([n,d])
    dx = [-1, 1]
    visited = [False for _ in range(5)]
    visited[n] = True
    while deq:
        loc, dir = deq.popleft()
        rotate(loc, dir)
        
        for move in dx:
            nxt = move + loc
            if not (1 <= nxt <= 4): continue
            if not relation[loc][nxt]: continue
            if visited[nxt]: continue
            deq.append([nxt, -dir])
            visited[nxt] = True
    

def rotate(n,d):
    if d == 1:
        gears[n].appendleft(gears[n].pop())
    else:
        gears[n].append(gears[n].popleft())
        


if __name__ == "__main__":
    gears = [None]
    for i in range(4):
        gears.append(deque(list(input().strip())))
    
    k = int(input())
    for i in range(k):
        n, d = map(int, input().split())
        operation(n,d)
    
    score = 1
    answer = 0
    for i in range(1,5):
        if gears[i][0] == '1':
            answer += score
        score *= 2
    
    print(answer)