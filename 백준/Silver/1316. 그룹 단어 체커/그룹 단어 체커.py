from sys import stdin

n = int(stdin.readline())
a = [stdin.readline() for i in range(n)]
total = 0
for i in range(len(a)):
    tutu = 0
    z = []
    for j in range(len(a[i])):
        u = a[i][j]
        if u in z and u != a[i][j-1]:
            break
        else:
            z.append(u)
            tutu += 1

    if tutu == len(a[i]):
        total += 1

print(total)
