from sys import stdin

n = int(stdin.readline())
u = []
stack = []

for i in range(n):
    u.append(stdin.readline().split())
    if u[i][0] == "push":
        stack.append(int(u[i][1]))
    elif u[i][0] == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif u[i][0] == 'size':
        print(len(stack))
    elif u[i][0] == "empty":
        if len(stack) ==0:
            print(1)
        else:
            print(0)
    elif u[i][0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[len(stack)-1])