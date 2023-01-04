t = int(input())
d = []
for i in range(t):
    c = str(input())
    a = c[0]
    b = c[2]
    d.append(int(a)+int(b))

for i in range(len(d)):
    print(d[i])