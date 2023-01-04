from sys import stdin

a,b = map(int, stdin.readline().split())
c = int(stdin.readline())

if b+c >= 60:
    a += (b+c)//60
    b = (b+c)%60
    if a >= 24:
        a -= 24
else:
    b += c

print(str(a)+" "+ str(b))