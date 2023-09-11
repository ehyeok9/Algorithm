import sys
input = sys.stdin.readline
from collections import deque

mini = 95678430120
maxi = 0

def check(equality, chosen):
    if (len(chosen) < 2): return True
    for i in range(len(chosen)-1):
        if ((equality[i] == '<') and chosen[i] < chosen[i+1]): continue
        if ((equality[i] == '>') and chosen[i] > chosen[i+1]): continue
        return False
    return True

def calc(chosen):
    val = 0 
    for i in range(len(chosen)-1,-1,-1):
        val += pow(10, len(chosen)-1-i)*chosen[i]
    return val

def backTracking(equality, num, cases, chosen, visited, r):
    global maxi, mini
    if (len(chosen) == r):
        if (check(equality, chosen)):
            val = calc(chosen)
            if (val > maxi): maxi = val
            if (val < mini): mini = val
        return
    if (not check(equality, chosen)): return
    
    for i in range(len(num)):
        if (not visited[i]):
            chosen.append(num[i])
            visited[i] = True
            backTracking(equality, num, cases, chosen, visited, r)
            visited[i] = False
            chosen.pop()
    
def makeString(val, r):
    if (len(str(val)) == r): return val
    string = str(val)
    while (len(string) != r):
        string = "0" + string
    return string
    


if __name__ == "__main__":
    k = int(input())
    equality = list(input().split())
    num = [i for i in range(10)]
    cases = []
    visited = [False for i in range(10)]
    
    backTracking(equality, num, [], [], visited, k+1)
    
    print(makeString(maxi, k+1))
    print(makeString(mini, k+1))
    
    
    
            