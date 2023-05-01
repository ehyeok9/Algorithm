import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    input = list(map(int, sys.stdin.readline().split()))
    input.sort()
    
    if (len(input)%2 == 1): print(input[len(input)//2])
    else:
        one = input[len(input)//2]
        two = input[len(input)//2-1]
        print(two)
        