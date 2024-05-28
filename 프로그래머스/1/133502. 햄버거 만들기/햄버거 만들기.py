def solution(ingredient):
    answer = 0
    
    stack = []
    for i in range(len(ingredient)):
        stack.append(ingredient[i])
        if judge(stack):
            popping(stack)
            answer += 1
            
    return answer

def judge(stack):
    return stack[-4:] == [1,2,3,1]

def popping(stack):
    for i in range(4): 
        stack.pop()