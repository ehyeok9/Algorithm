import sys
from collections import deque

input = sys.stdin.readline

def D(data):
    return (2*data) % 10000
        
def S(data):
    if (data == 0):
        return 9999
    return data - 1

def L(data):
    d1 = (data // 1000)
    d2 = (data // 100) % 10
    d3 = (data // 10) % 10
    d4 = data % 10

    return (d2 * 1000) + (d3 * 100) + (d4 * 10) + d1
def R(data):
    d1 = (data // 1000)
    d2 = (data // 100) % 10
    d3 = (data // 10) % 10
    d4 = data % 10
    return (d4 * 1000) + (d1 * 100) + (d2 * 10) + d3

def bfs(origin, target):
    deq = deque()
    commands = [D, S, L, R]
    letters = ["D", "S", "L", "R"]
    deq.append(origin)
    visited = set()
    used = dict()
    
    while deq:
        data = deq.popleft()
        if (data == target):
            return reconstruct(used, origin, target)
        
        for i in range(4):
            next_data = commands[i](data)
            if (next_data in visited):
                continue
            deq.append(next_data)
            visited.add(next_data)
            used[next_data] = (data, letters[i])

def reconstruct(used, origin, target):
    path = []
    current = target
    
    while (current != origin):
        prev, command = used[current]
        path.append(command)
        current = prev
    
    path.reverse()
    return "".join(path)

if __name__ == "__main__":
    t = int(input())
    
    for _ in range(t):
        origin, target = map(int, input().split())
        
        print(bfs(origin, target))