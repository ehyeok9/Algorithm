def solution(N, stages):
    stages.sort()
    answer = []
    
    temp = []
    total = len(stages)
    prev = 1
    count = 0
    for num in stages:
        if num != prev:
            temp.append([count/total, prev])
            total -= count
            prev += 1
            while prev != num:
                temp.append([0, prev])
                prev += 1
            count = 1
        else:
            count += 1
    
    if prev <= N:
        temp.append([count/total, prev])
        prev += 1
        
    while prev <= N:
        temp.append([0, prev])
        prev += 1
    
    temp.sort(reverse=True, key = lambda x : (x[0], -x[1]))
    
    answer = [val[1] for val in temp]
    
    return answer