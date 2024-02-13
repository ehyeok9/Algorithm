import sys

input = sys.stdin.readline

global n, s, arr

seq = 100000
result = float("inf")

def findLeastSequence(start, end):
    global seq
    if start >= end:
        return
    
    if sum(arr[start:end]) >= s:
        if end-start < seq:
            seq = end - start
    
    mid = (start+end)//2
    
    findLeastSequence(start, mid)
    findLeastSequence(mid+1, end)
    
    for i in range(mid, -1, -1):
        if sum(arr[i: mid]) >= s and i + mid < seq:
            seq = i + mid
            break
    
    for i in range(mid, len(arr), 1):
        if sum(arr[mid: i]) >= s and i - mid < seq:
            seq = i - mid
            break

def sequence():
    global seq, result
    this, i = 0, 0
    for j in range(n):
        this += arr[j]
        if this >= s:
            seq = j-i+1 
            for k in range(i, j):
                this -= arr[k]
                if this >= s: 
                    seq -=1
                else:
                    i = k+1 
                    break
                
            if seq < result:
                result = seq

            
    
    

if __name__ == "__main__":
    n, s = map(int, input().split())
    arr = list(map(int, input().split()))
    
    sequence()
    
    if result == float("inf"):
        print(0)
    else:
        print(result)