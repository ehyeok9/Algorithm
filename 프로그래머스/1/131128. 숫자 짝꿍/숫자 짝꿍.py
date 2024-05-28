def solution(X, Y):
    countX = [0 for _ in range(10)]
    countY = [0 for _ in range(10)]
    
    for i in range(len(X)):
        countX[int(X[i])] += 1
    for i in range(len(Y)):
        countY[int(Y[i])] += 1
        
    setX = set(X)
    setY = set(Y)
    
    nums = []
    intersection = list(setX & setY)
    for num in intersection:
        nums.extend([num] * min(countX[int(num)], countY[int(num)]))
    
    nums.sort(reverse=True)
    
    if nums == []:
        return "-1"
    if nums[0] == '0':
        return "0"
    return "".join(nums)