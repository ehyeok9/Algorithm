from sys import stdin

s = input()
lit = []

for i in range(len(s)):
    lit.append(s[i:])

for i in sorted(lit):
    print(i)