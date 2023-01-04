from sys import stdin

a = int(stdin.readline())
b = int(stdin.readline())
c = int(stdin.readline())

u = str(a*b*c)

for i in range(0, 10):
    sum = 0
    for j in range(len(u)):
        if i == int(u[j]):
            sum += 1
    print(sum)
