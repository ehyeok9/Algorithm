import sys
input = sys.stdin.readline
from collections import deque

def swap(inp, fr, to):
    temp = inp[fr]
    inp[fr] = inp[to]
    inp[to] = temp
    return

if __name__ == "__main__":
    n, m = map(int, input().split())
    basket = [i for i in range(n+1)]
    
    for i in range(m):
        start, end = map(int, input().split())
        temp = basket[start:end+1][::-1]
        basket[start: end+1] = temp
    
    print(*basket[1:])