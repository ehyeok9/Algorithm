import sys
input = sys.stdin.readline
from collections import deque
    
if __name__ == "__main__":
    n = int(input())
    dic = {}
    
    for i in range(n):
        name, order = map(str, input().split())
        if (order == "enter"):
            dic[name] = True
        else: 
            del dic[name]
    
    
    for name in sorted(dic.keys(), reverse=True):
        print(name)
    