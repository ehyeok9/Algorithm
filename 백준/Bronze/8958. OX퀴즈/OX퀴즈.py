from sys import stdin

n = int(stdin.readline())
a = []

for i in range(n):
    u = stdin.readline()
    total = 0
    h = 1
    for j in range(len(u)):
        if u[j] == "O":
            total += h
            h += 1
        else:
            h = 1

    a.append(total)

for i in a:
    print(i)
