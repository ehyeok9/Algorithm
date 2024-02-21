def solution(n, arr1, arr2):
    answer = []
    
    board1 = []
    for line in arr1:
        board1.append(convert(line, n))
    
    board2 = []
    for line in arr2:
        board2.append(convert(line, n))
    
    
    for i in range(n):
        temp = []
        for j in range(n):
            if board1[i][j] == 0 and board2[i][j] == 0:
                temp.append(" ")
            else:
                temp.append("#")
        answer.append("".join(temp))
    
    return answer

def convert(num, n):
    temp = []
    while num > 0 :
        temp.append(num % 2)
        num //= 2
    
    while len(temp) < n:
        temp.append(0)
    
    return list(reversed(temp))