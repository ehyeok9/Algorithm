from sys import stdin

u = stdin.readline()
a = ""

for i in range(len(u)):
    q = ord(u[i])
    if (96<q<123) or (64 < q < 91):
        j = q + 13
        if (96<q<123) and j >122:
            a += chr(j-26)
        elif (96<q<123) and (96<j<123):
            a += chr(j)
        elif (64 < q < 91) and j > 90:
            a += chr(j-26)
        else:
            a += chr(j)
    else:
        a += chr(q)

print(a)
