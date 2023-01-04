from sys import stdin

n = int(stdin.readline())
answer = 0
i = 1
while i <= n:
    answer += (n-i+1)
    i *= 10
print(answer)


