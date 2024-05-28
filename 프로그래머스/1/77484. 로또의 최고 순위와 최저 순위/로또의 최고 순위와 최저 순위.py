def solution(lottos, win_nums):
    visited = set()
    
    for num in lottos:
        if num in win_nums:
            visited.add(num)
    
    mini = len(visited)
    maxi = mini + lottos.count(0)
    
    dictionary = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    
    return [dictionary[maxi], dictionary[mini]]