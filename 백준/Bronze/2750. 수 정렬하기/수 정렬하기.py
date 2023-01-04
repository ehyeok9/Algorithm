t = int(input())

n = [int(input()) for i in range(t)]

n.sort()

for i in range(len(n)):
    print(n[i])