import sys
input = sys.stdin.readline

global answer

def dp(a, b, num):
    global answer
    if (a > b): return
    if (a == b): 
        if (num < answer):
            answer = num
        return
    dp(a*2, b, num+1)
    dp(a*10+1, b, num+1)
    
    
if __name__ == "__main__":
    a, b = map(int, input().split())
    answer = pow(10, 8)
    
    dp(a, b, 0)
    
    if (answer == pow(10, 8)):
        print(-1)
    else:   
        print(answer+1)
    