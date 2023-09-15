import sys
input = sys.stdin.readline
from collections import deque

if __name__ == "__main__":
    n = int(input())
    m = int(input())
    s = input().rstrip()
    
    p = "IOI" + "OI"*(n-1)
    length = len(p)
    cnt = 0
    
    # print(m-length)
    for i in range(0, m-length+1):
        if (s[i:i+length] == p):
            cnt += 1
            
    print(cnt)