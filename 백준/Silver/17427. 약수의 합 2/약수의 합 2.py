import sys
import math

input = sys.stdin.readline

def getSum(number):
    total = 0
    for i in range(1, number+1):
        total += i * (number//i)
    return total

if __name__ == "__main__":
    num = int(input())
    print(getSum(num))