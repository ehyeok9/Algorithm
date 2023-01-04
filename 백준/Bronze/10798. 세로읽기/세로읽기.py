from sys import stdin

q = []
u = []

for i in range(5):
    w = input()
    q.append(w)
    u.append(len(w))

for i in range(5):
    if len(q[i]) != max(u):
        q[i] += (" "*(max(u)-len(q[i])))

for i in range(len(q[0])):
    for j in range(5):
        if q[j][i] != " ":
            print(q[j][i], end="")


