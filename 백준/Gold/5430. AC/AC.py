import sys

input = sys.stdin.readline

def execute(command, arr):
    flag = True
    start = 0
    end = len(arr)
    
    for i in range(len(command)):
        if (command[i] == "R"):
            flag = not flag
        else:
            if (start == end):
                print("error")
                return
            if (flag):
                start += 1
            else: 
                end -= 1
    result = arr[start:end]
    
    print("[", end = "")
    if (flag):
        print(*result, sep = ",", end = "]\n")
    else:
        print(*result[::-1], sep = ",", end = "]\n")
    
if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        Command = list(input().rstrip())
        n = int(input())
        arr = input().rstrip().split(",")
        arr[0] = arr[0][1:]
        arr[-1] = arr[-1][:-1]
        
        if (n == 0):
            arr = []
        
        execute(Command, arr)