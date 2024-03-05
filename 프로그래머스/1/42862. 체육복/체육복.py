def solution(n, lost, reserve):
    answer = n - len(lost)
    
    reserve.sort()
    lost.sort()
    for val in reserve:
        if val in lost:
            answer += 1
            lost.remove(val)
            continue
            
        if val - 1 in lost:
            answer += 1
            lost.remove(val-1)
            continue
            
        if val + 1 in lost and (val+1) not in reserve:
            answer += 1
            lost.remove(val+1)
            
        
    return answer