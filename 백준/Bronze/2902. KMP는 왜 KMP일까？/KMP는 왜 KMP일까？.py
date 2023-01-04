s = input()

a = []
for i in range(len(s)):
    if 65 <= ord(s[i]) <=90:
        a.append(s[i])
    
for i in range(len(a)):
    print(a[i], end="")