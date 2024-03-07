def solution(n):
    answer = 0
    converted = numTo3(n)
    
    idx = 0
    for i in range(len(converted)-1, -1, -1):
        answer += converted[i] * pow(3, idx)
        idx += 1
        
    return answer


def numTo3(num):
    result = []
    
    while (num > 0):
        result.append(num%3)
        num //= 3
    # result.append(num)
    return result