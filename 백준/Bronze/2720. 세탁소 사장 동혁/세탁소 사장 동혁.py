import sys
input = sys.stdin.readline
from collections import deque
    
if __name__ == "__main__":
    t = int(input())
    
    for i in range(t):
        dollar = int(input())
        
        q = dollar//25
        dollar -= q*25
        
        d = dollar//10
        dollar -= d*10
        
        n = dollar//5
        dollar -= n*5
        
        p = dollar
        
        print(q,d,n,p)