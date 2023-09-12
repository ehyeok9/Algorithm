import sys
input = sys.stdin.readline
from collections import deque

if __name__ == "__main__":
    lit = list(map(int, input().split()))
    print(sum(lit))