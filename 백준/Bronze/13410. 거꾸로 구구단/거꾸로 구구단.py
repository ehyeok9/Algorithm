n, k = map(int, input().split())

a = []
b = []

for i in range(1, k+1):
    a.append(str(i*n))
    x = a[i-1]
    if int(x) >= 10:
        x = x[::-1]
        b.append(int(x))
    else:
        b.append(int(x))

print(max(b))