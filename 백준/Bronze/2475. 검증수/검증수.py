from sys import stdin

def gegg(n):
    return n**2

a, b, c, d, e = map(int, stdin.readline().split())
t = [a,b,c,d,e]
u = []
for i in t:
    u.append(gegg(i))

print(sum(u)%10)