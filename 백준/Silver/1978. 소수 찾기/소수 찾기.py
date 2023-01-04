from sys import stdin

def find(n):
    if n == 1:
        return 0;
    for i in range(2,n+1):
        if n%i == 0:
            if i != n:
                return 0
            else:
                return 1

t = int(stdin.readline())
lit = list(map(int, stdin.readline().split()))
total = 0

for i in lit:
    total += find(i)

print(total)