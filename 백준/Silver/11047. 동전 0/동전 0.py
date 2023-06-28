import sys
from collections import deque

def minus(coin, k, ans):
    ans += (k//coin)
    k -= (k//coin)
    return k, ans

    
if __name__=="__main__":
    n, k = map(int, sys.stdin.readline().split())
    input = []
    ans = 0
    for i in range(n):
        input.append(int(sys.stdin.readline()))
    
    for i in range(n-1, -1, -1):
        coin = input[i]
        if (k >= coin):
            temp = k//coin
            k -= coin*temp
            ans += temp
    
    print(ans)