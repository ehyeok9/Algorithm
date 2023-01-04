n = str(input())

a = [ ":fan:" for i in range(8) ]

a.insert(4, ":"+n+":")

for i in range(len(a)):
    if i == 3 or i == 6:
        print()
    print(a[i], end="")
