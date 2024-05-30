def solution(survey, choices):
    score = [0, 0, 0, 0]
    types = ["RT", "CF", "JM", "AN"]
    
    for i in range(len(survey)):
        quest = survey[i]
        for j in range(4):
            val = types[j]
            if quest == val and choices[i] < 4:
                score[j] -= (4 - choices[i])
            elif quest == val and choices[i] > 4:
                score[j] += (choices[i] - 4)
            elif quest == val[::-1] and choices[i] < 4:
                score[j] += (4 - choices[i])
            elif quest == val[::-1] and choices[i] > 4:
                score[j] -= (choices[i] - 4)
                
        print(score)
            
    answer = ""
    for i in range(4):
        if score[i] <= 0:
            answer += types[i][0]
        else:
            answer += types[i][1]

    return answer