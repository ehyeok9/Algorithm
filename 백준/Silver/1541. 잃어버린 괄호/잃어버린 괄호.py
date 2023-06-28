import sys

if __name__=="__main__":
    input = sys.stdin.readline()
    lit = input.split("-")
    minus = []
    
    for phase in lit:
        temp = phase.split("+")
        ans = 0
        for num in temp:
            ans += int(num)
        minus.append(ans)
    
    result = minus[0]
    for i in range(1,len(minus)):
        result -= int(minus[i])
    print(result)