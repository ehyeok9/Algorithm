def solution(data, ext, val_ext, sort_by):
    answer = []
    dictionary = {"code": 0, "date": 1, "maximum": 2, "remain": 3}
    col = dictionary[ext]
    
    for row in data:
        if row[col] < val_ext:
            answer.append(row)
    answer.sort(key = lambda x : x[dictionary[sort_by]])
    return answer