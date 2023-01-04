from sys import stdin

c = int(stdin.readline())
q = []

for i in range(c):
    q.append(list(map(int,stdin.readline().split())))

for i in range(len(q)):
    be = sum(q[i][1:])/q[i][0]
    total = 0
    for j in range(q[i][0]):
        if q[i][j+1] > be:
            total += 1
    print("%.3f" % ((total/q[i][0])*100)+"%")