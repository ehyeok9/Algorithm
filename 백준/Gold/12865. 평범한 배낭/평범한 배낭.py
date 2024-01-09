import sys

input = sys.stdin.readline

def dp(n, weight, items):
    memo = [0 for _ in range(weight+1)]
    items.sort()
    
    for i in range(n):
        iw, iv = items[i]
        for j in range(weight, iw-1, -1):
            memo[j] = max(memo[j], memo[j-iw]+iv)
            
    return memo[weight]
        
if __name__ == "__main__":
    n, k = map(int, input().split())
    items = [ list(map(int, input().split())) for _ in range(n)]
    
    print(dp(n, k, items))
    