def solution(players, callings):
    answer = []
    mapper = dict()
    for i in range(len(players)):
        mapper[players[i]] = i
        
    for name in callings:
        idx = mapper[name]
        mapper[name] -= 1
        players[idx - 1], players[idx] = players[idx], players[idx-1]
        mapper[players[idx]] += 1
    
    # print(players)
    return players