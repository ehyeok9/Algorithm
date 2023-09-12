import sys
input = sys.stdin.readline
from collections import deque

if __name__ == "__main__":
    inp = []
    for i in range(20):
        temp = list(input().split())
        inp.append(temp)
        
    dic = {'A+':4.5, 'A0': 4.0, 'B+':3.5, 'B0': 3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0, 'P':0}
    answer = 0
    num = 0
    
    for lit in inp:
        su = float(lit[1])
        grade = dic[lit[2]]
        if (lit[2] == 'P'): continue
        num += su
        answer += su * grade
    
    print("{:.6f}".format(answer/num))
    