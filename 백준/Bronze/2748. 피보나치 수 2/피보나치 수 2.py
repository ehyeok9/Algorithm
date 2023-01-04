from sys import stdin

n = int(stdin.readline())
fibo = [0,1]

if n < 2:
    print(fibo[n])
else:
    for i in range(2, n+1):
        fibo.append(fibo[i-1]+fibo[i-2])
    print(fibo.pop())