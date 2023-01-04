from sys import stdin

a = stdin.read()
b = []

for i in range(len(a)):
    b.append(a[i])

b.sort(reverse=True)
print("".join(b))