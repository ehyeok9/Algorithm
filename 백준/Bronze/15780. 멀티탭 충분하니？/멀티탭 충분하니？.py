n, k = map(int, input().split())

a = list(map(int, input().split()))

sum = 0

for i in range(len(a)):
    if a[i] == 3 or a[i]==4:
        sum += 2
    elif a[i] == 5 or a[i] == 6:
        sum += 3
    else:
        sum += 4
if sum >= n:
    print("YES")
else:
    print("NO")