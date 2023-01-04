def yuk(a,b,c,d):
    u = a+b+c+d
    f = ["D","C","B","A","E"]
    print(f[u])

for i in range(3):
    a,b,c,d = map(int, input().split())
    yuk(a,b,c,d)
