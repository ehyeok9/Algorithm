import sys
input = sys.stdin.readline
from collections import deque
from string import ascii_uppercase

if __name__ == "__main__":
    for line in sys.stdin:
        n = int(line)
        temp = 1
        while (temp%n != 0):
            temp *= 10
            temp += 1
        print(len(str(temp)))