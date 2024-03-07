def solution(a, b):
    d = [0,31,29,31,30,31,30,31,31,30,31,30,31]
    day = {1: "FRI", 2: "SAT", 3: "SUN", 4: "MON", 5: "TUE", 6:"WED", 0:"THU"}
    
    total = 0
    for i in range(a):
        total += d[i]
    total += b
    
    return day[total%7]