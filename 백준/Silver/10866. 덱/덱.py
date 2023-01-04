from sys import stdin
queue = []

def exist(q):
    if len(q) == 0:
        return False
    else:
        return True

def dec(n):
    global queue
    if len(n) == 2:
        if n[0] == "push_back":
            queue.append(n[-1])
        elif n[0] == "push_front":
            queue.insert(0, n[-1])
    else:
        if n[0] == "size":
            print(len(queue))
        elif n[0] == "empty":
            if exist(queue):
                print(0)
            else:
                print(1)
        elif n[0] == "front":
            if exist(queue):
                print(queue[0])
            else:
                print(-1)
        elif n[0] == "back":
            if exist(queue):
                print(queue[len(queue)-1])
            else:
                print(-1)
        elif n[0] == "pop_front":
            if exist(queue):
                print(queue[0])
                del queue[0]
            else:
                print(-1)
        elif n[0] == "pop_back":
            if exist(queue):
                print(queue.pop())
            else:
                print(-1)


n = int(stdin.readline())

for i in range(n):
    u = stdin.readline().split()
    dec(u)