n = int(input())

for i in range(n-1, 0, -1):
    print("*"*(n-i)+" "*(2*i)+"*"*(n-i))
print("*"*2*n)
for i in range(1, n+1):
    print("*"*(n-i)+" "*(2*i)+"*"*(n-i))