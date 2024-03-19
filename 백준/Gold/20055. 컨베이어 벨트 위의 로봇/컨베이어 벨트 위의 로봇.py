import sys
from collections import deque

input = sys.stdin.readline

global n, k, durability, cnt    

if __name__ == "__main__":
    n, k = map(int, input().split())
    
    belt = list(map(int, input().split()))
    for i in range(2*n):
        belt[i] = [0, belt[i]]
    belt = deque(belt)
    step, cnt = 1, 0
    
    while True:
        belt.rotate(1)
        if belt[n-1][0] != 0:
            belt[n-1][0] = 0
            
        # print(1, belt)
        for cur in range(n-2, 0, -1):
            nxt = (cur+1) % (2*n)
            if belt[cur][0] != 0 and belt[nxt][0] == 0 and belt[nxt][1] >= 1:
                belt[nxt][1] -= 1
                belt[nxt][0] = 1
                belt[cur][0] = 0
                
                if belt[nxt][1] == 0:
                    cnt += 1

            if belt[n-1][0] != 0:
                belt[n-1][0] = 0
                
        # print(2, belt)
        if belt[0][1] >= 1:
            belt[0][0] = 1
            belt[0][1] -= 1

            if belt[0][1] == 0:
                cnt += 1
        # print(3, belt)
        if cnt >= k: break
        step += 1
        
    
    print(step)
        
            
            
        
        
    
    
    