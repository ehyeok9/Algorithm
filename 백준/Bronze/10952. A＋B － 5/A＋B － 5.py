u = []
def infinity():
    while True:
        yield

for i in infinity():
    a,b = map(int, input().split())
    if (a == 0) and (b ==0) :
        break
    u.append(a+b)

for number in u:
    print(number)