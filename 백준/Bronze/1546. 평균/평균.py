n = int(input())

a = list(map(int, input().split()))

m = max(a)

for i in range(n):
    a[i] = ((a[i] / m)*100)

sum = sum(a) / len(a)

print("%.2f"%sum)
