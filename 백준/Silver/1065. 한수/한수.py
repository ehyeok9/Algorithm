n = int(input())

sum = 0
sum2 = 99

if n < 100:
    print(n)
elif n >= 100:
    for i in range(100, n+1):
        u =[int(i) for i in str(i)]
        for j in range(-4, 5):
            if str(i) == "{}{}{}".format(u[0], u[0] + j, u[0] + 2*j):
                sum2 += 1
    print(sum2)