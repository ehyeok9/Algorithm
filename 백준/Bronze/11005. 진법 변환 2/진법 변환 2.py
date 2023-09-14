import sys
input = sys.stdin.readline
from collections import deque
from string import ascii_uppercase

if __name__ == "__main__":
    n, b = map(int, input().split())
    nameogi = []
    
    while (n >= b):
        nameogi.append(n%b)
        n //= b
    nameogi.append(n)
    
    dic = {}
    for i in range(10):
        dic[i] = str(i)
    
    for idx, alpha in enumerate(ascii_uppercase):
        dic[idx+10] = alpha
    
    answer = ""
    for num in reversed(nameogi):
        answer += dic[num]
    
    print(answer)