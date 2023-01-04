x = int(input())
a = 1
while (x > a):
    x -= a
    a += 1

b = []
for i in range(1, a+1):
    z = (i, a+1 - i)
    b.append(z)
if a % 2 == 0 :
    print(str(b[x-1][0]) + "/" + str(b[x-1][1]))
else:
    print(str(b[x - 1][1]) + "/" + str(b[x - 1][0]))