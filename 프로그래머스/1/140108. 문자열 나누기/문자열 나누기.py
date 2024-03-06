def solution(s):
    answer = 0
    
    while s != "":
        # print(s, answer)
        s = nxtString(s)
        answer += 1
        # print(s, answer)
    
    return answer

def nxtString(string):
    first = string[0]
    scnt, dcnt = 1,0
    for i in range(1, len(string)):
        if string[i] == first:
            scnt += 1
        else:
            dcnt += 1
        
        if scnt == dcnt:
            return string[i+1:]
    
    return ""
        
    