s = input()

a = [-1 for i in range(26)]

for i in range(len(s)):
    for j in range(97, 123):
        if (ord(s[i])==j) and (a[j-97] == -1):
            a[j - 97] = i



for i in range(len(a)):
    print(a[i], end=" ")
