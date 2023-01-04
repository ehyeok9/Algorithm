s = input()

sum = 0

if s[0]== " " and s[len(s)- 1] == " ":
    for i in range(len(s)):
        if s[i] == " ":
            sum += 1
    print(sum - 1)
elif s[0] == " " or s[len(s) -1] == " ":
    for i in range(len(s)):
        if s[i] == " ":
            sum += 1
    print(sum)
else:
    for i in range(len(s)):
        if s[i] == " ":
            sum += 1
    print(sum+1)