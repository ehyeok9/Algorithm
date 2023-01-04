k, n, m = map(int, input().split())

total = k*n

if m >= total:
    print(0)
else:
    print(total-m)