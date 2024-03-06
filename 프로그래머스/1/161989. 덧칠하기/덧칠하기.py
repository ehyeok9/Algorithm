def solution(n, m, section):
    answer = 0
    idx = 1
    pointer = 0
    while idx <= n and pointer <= len(section) - 1:
        if idx == section[pointer]:
            answer += 1
            idx += m
            while pointer < len(section):
                if section[pointer] < idx:
                    pointer += 1
                else:
                    break
        else:
            idx += 1
    return answer