from sys import stdin
memo = {}

def fibo(n):
    if n in memo:
        return memo[n]
    if n == 0:
        memo[n]=0
    elif n == 1 or n == 2:
        memo[n] = 1
    else:
        memo[n] = fibo(n-1) + fibo(n-2)
    return memo[n]

n = int(stdin.readline())

print(fibo(n))