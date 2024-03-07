import math

def solution(number, limit, power):
    answer = 0
    for i in range(1, number +1):
        temp = getMeasure(i)
        if temp > limit:
            answer += power
        else:
            answer += temp              
        
    return answer

def getMeasure(num): 
    result = 0
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            if pow(i, 2) == num:
                result += 1
            else:
                result += 2
    return result