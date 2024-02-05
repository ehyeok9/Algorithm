import sys
from collections import deque

input = sys.stdin.readline

global arr, string, length

def divideConquer():
    sin, sout = [], deque(arr)
    
    while sout:
        sin.append(sout.popleft())
        ls = len(sin)
        if (ls >= length):
            for i,j in zip(string, sin[ls - length:]):
                if i != j:
                    break
            else:
                for _ in range(length):
                    sin.pop()
                
        
    if sin == []:
        print("FRULA")
    else:
        print("".join(sin))
            
        
            
     
    

if __name__ == "__main__":
    arr = list(input().strip())
    string = list(input().strip())
    length = len(string)
    
    divideConquer()