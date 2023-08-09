import sys

def combination(arr, r):
    result = []
    if r == 0:
        return [[]]
    
    for i, elem in enumerate(arr):
        elem = arr[i]
        rest_arr = arr[i+1:]
        for c in combination(rest_arr, r-1):
            result.append([elem] + c)
            
    return result

def distance(prev, cur):
    cnt = 0 
    
    for i in range(4):
        if (prev[i] != cur[i]): cnt += 1
    return cnt

if __name__=="__main__":
    t = int(sys.stdin.readline())
    
    for i in range(t):
        num = int(sys.stdin.readline())
        arr = list(sys.stdin.readline().split())
        dic = {}
        for val in arr:
            if val in dic.keys():
                dic[val] = dic[val] + 1
            else:
                dic[val] = 1
        arr = []
        flag = False        
        for val in dic.keys():
            if (dic[val] >= 3):
                flag = True
                break
            else:
                for i in range(dic[val]):
                    arr.append(val)
        if (flag):
            print(0)
            continue
        result = combination(arr, 3)
        
        minimum = 200
        for ins in result:
            prev = ins[2]
            cnt = 0
            for cur in ins:
                cnt += distance(prev, cur)
                prev= cur
            if (cnt < minimum): minimum = cnt
        
        print(minimum)
    
        