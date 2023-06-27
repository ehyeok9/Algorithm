import sys

def round2(num):
    answer = int(num)
    temp = 1 if (num - answer) >= 0.5 else 0 
    return answer + temp

if __name__=="__main__":
    n = int(sys.stdin.readline())
    input = []
    for i in range(n):
        input.append(int(sys.stdin.readline()))
    input.sort()
    
    val = round2(n * 0.15)
    input = input[val: n-val]
    if (len(input) == 0):
        print(0)
    else:
        result = round2(sum(input)/len(input))
        print(result)