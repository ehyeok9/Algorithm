import sys

input = sys.stdin.readline

def multiply(a, b, c):
    if (b == 1):
        return a % c
    else:
        temp = multiply(a, b // 2, c)
        if (b % 2 == 0):
            return temp * temp % c
        else:
            return temp * temp * a % c

if __name__ == "__main__":
    a, b, c = map(int, input().split())
    
    print(multiply(a, b, c))