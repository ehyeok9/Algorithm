t = int(input())

result = []
for i in range(t):
    a,b = map(int, input().split())
    result.append(a+b)

for number in result :
    print(number)