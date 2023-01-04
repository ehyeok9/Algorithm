from sys import stdin

a = list(int(stdin.readline()) for i in range(10))
b = []

for i in a:
    b.append(i%42)

print(len(set(b)))