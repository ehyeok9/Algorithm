from collections import deque
import imp
import sys
from collections import deque

def getArr(num):
    answer = deque()
    while(num > 0):
        answer.appendleft(num%10)
        num //= 10
    return answer

if __name__ == "__main__":
    l, r = map(int, sys.stdin.readline().split())
    
    arrl = getArr(l)
    arrr = getArr(r)
    
    if (len(arrl) != len(arrr)):
        print(0)
    else:
        answer = 0
        while(arrl and arrr):
            lval = arrl.popleft() 
            rval = arrr.popleft()
            if (lval != rval): break
            if (lval == 8 and rval == 8): answer += 1
        print(answer)
    