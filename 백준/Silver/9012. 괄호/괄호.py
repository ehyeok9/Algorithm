t = int(input())

s = [input() for i in range(t)]

def pandan(s):
    sum1 =0
    sum2 =0
    for i in range(len(s)):
        if s[i] == "(":
            sum1 += 1
        else:
            sum2 +=1
        if sum2 > sum1:
            return "NO"
    if (sum1 == sum2) and s[0] == "(" and s[len(s)-1] ==")":
        return "YES"
    else:
        return  "NO"

for i in s:
    print(pandan(i))
