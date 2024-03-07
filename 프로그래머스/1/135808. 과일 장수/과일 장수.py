def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    idx = 0
    
    while idx+m <= len(score):
        answer += min(score[idx:idx+m]) * m
        idx += m
        
    return answer