import sys
from collections import deque

input = sys.stdin.readline

def calcBraket(line):
    stack = []
    for i in range(len(line)):
        if (line[i] != ')'):
            stack.append(line[i])
        else:
            temp = []
            while (True):
                if (stack[-1] == '('):
                    stack.pop()
                    break
                else:
                    temp.append(stack.pop())
            temp.reverse()
            stack.append(plusAndMinus(multiAndDivide(temp)))
    return stack
    
def multiAndDivide(arr):
    deq = deque(arr)
    stack = []
    while deq:
        if (deq[0] == '*' or deq[0] == '/'):
            prev = stack.pop()
            cur = deq.popleft()
            nxt = deq.popleft()
            stack.append("".join([prev, nxt, cur]))
        else:
            stack.append(deq.popleft())
    return stack

def plusAndMinus(arr):
    deq = deque(arr)
    stack = []
    while deq:
        if (deq[0] == '+' or deq[0] == '-'):
            prev = stack.pop()
            cur = deq.popleft()
            nxt = deq.popleft()
            stack.append("".join([prev, nxt, cur]))
        else:
            stack.append(deq.popleft())
    return "".join(stack)
        

if __name__ == "__main__":
    line = list(input())
    
    line = calcBraket(line)
    line = multiAndDivide(line)
    print(plusAndMinus(line))