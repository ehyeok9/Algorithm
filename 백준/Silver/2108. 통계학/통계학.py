from collections import Counter
from statistics import median
from sys import stdin

n = int(input())
m = list(int(stdin.readline()) for i in range(n))
u = sorted(m)

ran = max(m)-min(m)
sansul = sum(m)/len(m)
choibin = Counter(m).most_common()
h = []

if sansul > int(sansul) and sansul > 0:
    if (sansul*10) %10 >= 5:
        print(int(sansul)+1)
    else:
        print(int(sansul))
elif sansul < 0 and sansul < int(sansul):
    if (abs(sansul)*10)%10 >= 5:
        print(int(sansul)-1)
    else:
        print(int(sansul))
else:
    print(int(sansul))

print(median(m))
for num in choibin:
    if num[1] == choibin[0][1]:
        h.append(num[0])
h.sort()
if len(h) >= 2:
    print(h[1])
else:
    print(h[0])
print(ran)
