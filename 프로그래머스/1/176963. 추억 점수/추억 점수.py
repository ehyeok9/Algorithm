def solution(name, yearning, photo):
    answer = []
    mapper = dict()
    
    for na, ye in zip(name, yearning):
        mapper[na] = ye
        
    for lit in photo:
        temp = 0
        for val in lit:
            temp += mapper.get(val, 0)
        answer.append(temp)
        
    return answer