import math

answer = 0

def backtracking(idx, nums, visited, val, cnt):
    global answer
    if cnt == 3:
        if check(val):
            answer += 1
        return
        
    for i in range(idx, len(nums)):
        if visited[idx] == False:
            visited[idx] = True
            backtracking(i+1, nums, visited, val + nums[i], cnt + 1)
            visited[idx] = False

def check(val):
    if val == 2: return True
    for i in range(2, int(math.sqrt(val)) + 1):
        if val % i == 0:
            return False
    return True
    
def solution(nums):
    global answer
    nums = list(set(nums))
    visited = [False] * len(nums)
    
    backtracking(0, nums, visited, 0, 0)
    
    return answer