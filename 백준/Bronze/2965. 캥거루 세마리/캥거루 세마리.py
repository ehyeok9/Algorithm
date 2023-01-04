from sys import stdin

a,b,c = map(int, stdin.readline().split())

if c-b > b-a:
    print(c-b-1)
else:
    print(b-a-1)