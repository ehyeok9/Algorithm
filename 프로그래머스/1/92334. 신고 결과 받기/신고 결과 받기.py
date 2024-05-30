def solution(id_list, report, k):
    reportCount = dict(zip(id_list, [0] * len(id_list)))
    reportUser = dict(zip(id_list, [[] for _ in range(len(id_list))]))
    
    for content in report:
        fr, to = content.split()
        if to in reportUser[fr]: continue
        reportUser[fr].append(to)
        reportCount[to] += 1
    
    stop = []
    for user in id_list:
        if reportCount[user] >= k:
            stop.append(user)
    
    answer = []
    for user in id_list:
        cnt = 0
        people = reportUser[user]
        for person in people:
            if person in stop: cnt += 1
        answer.append(cnt)
        
    return answer