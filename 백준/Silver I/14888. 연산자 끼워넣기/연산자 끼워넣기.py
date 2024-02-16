import sys

input = sys.stdin.readline



def dfs(numbers, prev, idx):
    global add, sub, mul, div, N
    global maxi, mini
    
    if idx == N:
        maxi = max(maxi, prev)
        mini = min(mini, prev)
        return
    
    if add > 0:
        add -= 1
        dfs(numbers, prev + numbers[idx], idx + 1)
        add += 1
    if sub > 0:
        sub -= 1
        dfs(numbers, prev - numbers[idx], idx + 1)
        sub += 1
    if mul > 0:
        mul -= 1
        dfs(numbers, prev * numbers[idx], idx + 1)
        mul += 1
    if div > 0:
        div -= 1
        temp = 0
        if prev < 0:
            temp = -(-prev // numbers[idx])
        else:
            temp = prev // numbers[idx]
        dfs(numbers, temp, idx + 1)
        div += 1
        
if __name__ == "__main__":
    N = int(input())
    numbers = list(map(int, input().split()))
    add, sub, mul, div = map(int, input().split())
    
    maxi, mini = -float("inf"), float("inf")
    dfs(numbers, numbers[0], 1)
    print(maxi)
    print(mini)