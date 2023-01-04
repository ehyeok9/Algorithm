s = input()

cro = ["c=", "c-", "d-", "lj", "nj","s="]
sum = len(s)

for i in range(len(cro)):
    for j in range(len(s)-1):
        if cro[i] == s[j]+s[j+1]:
            sum -= 1

for k in range(len(s)-2):
    if "dz=" == s[k]+s[k+1]+s[k+2]:
        sum -= 2

for i in range(len(s)-1):
    if ("z=" == s[i]+s[i+1]) and (s[i-1] != "d"):
        sum -= 1

print(sum)