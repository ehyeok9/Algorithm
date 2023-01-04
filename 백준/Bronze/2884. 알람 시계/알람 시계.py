from sys import stdin

h,m = map(int, stdin.readline().split())

if (m >= 45):
    m -= 45
elif (h == 0):
    u = m-45
    m = 60 + u
    h = 23
else:
    u = m-45
    m =60 +u
    h -= 1

print(h, m)