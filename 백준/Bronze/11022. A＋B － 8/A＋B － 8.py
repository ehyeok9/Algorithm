t = int(input())
d = [0]
f = [0]
g = [0]
for i in range(t):
    a, b = map(int, input().split())
    d.append(a+b)
    f.append(a)
    g.append(b)

for i in range(1, len(d)):
    print("Case #{}: {} + {} = {}".format(i, f[i], g[i], d[i]))