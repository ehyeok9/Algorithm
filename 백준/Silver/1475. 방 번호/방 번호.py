from collections import Counter

n = input()
a = dict(Counter(n))

j = n.count("9")
k = n.count("6")

if (n.count("9")+n.count("6")) % 2 == 0:
    a["9"] = (j+k)//2
    a["6"] = (j+k) //2
else:
    a["9"] = (j+k) //2
    a["6"] = (j+k) //2 + 1

print(max(a.values()))
