def solution(numbers, hand):
    answer = ''
    
    left = (3,0)
    right = (3,2)
    
    for i in range(len(numbers)):
        if numbers[i] in [1,4,7]:
            answer += "L"
            left = getPosition(numbers[i])
        elif numbers[i] in [3,6,9]:
            answer += "R"
            right = getPosition(numbers[i])
        else:
            pos = getPosition(numbers[i])
            print(left, right, pos)
            ld, rd = getDistance(left, pos), getDistance(right, pos)
            print(ld, rd)
            if ld < rd:
                answer += "L"
                left = pos
            elif rd < ld:
                answer += "R"
                right = pos
            else:
                if hand == "right":
                    answer += "R"
                    right = pos
                else:
                    answer += "L"
                    left = pos
    return answer

def getDistance(a,b):
    return abs(a[0] - b[0])+abs(a[1] - b[1])


def getPosition(num):
    if num == 0:
        return (3,1)
    return ((num-1)//3, (num-1)%3)