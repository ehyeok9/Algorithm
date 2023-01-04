a =int(input())
b =int(input())
c =int(input())
d =int(input())
e =int(input())

f = [a, b, c, d, e]

for i in range(len(f)):
    if f[i] < 40:
        f[i] = 40

print(sum(f)//5)