n, x = map(int, input().split())

a = list(map(int, input().split()))

for i in range(len(a)):
    if x > a[i]:
        print(a[i], end=" ")

