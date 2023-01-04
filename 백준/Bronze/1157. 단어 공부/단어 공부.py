from sys import stdin
from collections import Counter

n = input().lower()
a = Counter(n).most_common()

if len(a) == 1:
    print(a[0][0].upper())
elif a[0][1] == a[1][1]:
    print("?")
else:
    print(a[0][0].upper())