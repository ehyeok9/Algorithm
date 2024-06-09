def solution(k, tangerine):
    answer = 0
    
    ranges = list(set(tangerine))
    classification = dict(zip(ranges, [0] * len(ranges)))
    for val in tangerine:
        classification[val] += 1;
    
    sorting = list(classification.items())
    sorting.sort(reverse=True, key=lambda x:x[1])
    
    for key,val in sorting:
        k -= val
        answer += 1
        if k <= 0:
            break
    
    return answer