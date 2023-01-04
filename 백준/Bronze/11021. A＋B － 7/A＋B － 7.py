t = int(input())
d = [0]

for i in range(t):
    a, b = map(int, input().split())
    d.append(a+b)

for i in range(1, len(d)):
    print("Case #{}: {}".format(i, d[i]))