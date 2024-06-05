def solution(friends, gifts):
    length = len(friends)
    result = [[0 for _ in range(length)] for _ in range(length)]
    direction = dict(zip(friends, [i for i in range(length)]))
    
    for instance in gifts:
        fr, to = instance.split()
        frIdx = direction[fr]
        toIdx = direction[to]
        result[frIdx][toIdx] += 1
    
    answer = [0 for _ in range(length)]
    for frIdx in range(length):
        for toIdx in range(frIdx, length):
            if frIdx == toIdx: continue
            sumation = result[frIdx][toIdx] - result[toIdx][frIdx]
            if sumation > 0:
                answer[frIdx] += 1
            elif sumation < 0:
                answer[toIdx] += 1
            else:
                frGiftIndex = sum(result[frIdx]) - sumCol(result, frIdx, length)
                toGiftIndex = sum(result[toIdx]) - sumCol(result, toIdx, length)
                if frGiftIndex > toGiftIndex:
                    answer[frIdx] += 1
                elif frGiftIndex < toGiftIndex:
                    answer[toIdx] += 1
                    
    return max(answer)

def sumCol(result, idx, length):
    answer = 0
    for i in range(length):
        answer += result[i][idx]
    return answer