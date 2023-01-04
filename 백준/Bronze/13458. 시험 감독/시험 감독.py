n = int(input())
a = list(map(int, input().split()))
b,c = map(int, input().split())

sum = 0

for i in range(len(a)):
    if b >= a[i]:
        sum += 1
    else:
        a[i] -= b
        sum += 1
        if a[i] % c == 0:
            sum += a[i]//c
        else:
            sum += a[i]//c + 1

print(sum)