def facto(n):
    if n == 0:
        return 1
    return n*facto(n-1)

n = int(input())

x = str(facto(n))

sum = 0

for i in range(len(x)-1, 0, -1):
    if x[i] == "0":
        sum +=1
    else:
        break
print(sum)