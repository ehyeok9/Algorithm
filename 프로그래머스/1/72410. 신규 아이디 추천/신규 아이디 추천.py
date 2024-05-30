def solution(new_id):
    temp = toLower(new_id)
    temp = removeOther(temp)
    temp = substitution(temp)
    temp = removeStrip(temp)
    temp = insertValue(temp)
    temp = removeUpper15(temp)
    temp = extendString(temp)    
    
    return "".join(temp)

def toLower(arr):
    return arr.lower()

def removeOther(arr):
    result = []
    allow = ['-', '_', '.']
    for char in arr:
        if ('a' <= char <= 'z') or (char in allow) or ('0' <= char <= '9'):
            result.append(char)
    return result

def substitution(arr):
    result = []
    flag = False
    for char in arr:
        if flag and (char == '.'): continue
        result.append(char)
        
        if (char == '.'): 
            flag = True
        else:
            flag = False
    return result

def removeStrip(arr):
    if arr and (arr[0] == '.'): arr.pop(0)
    if arr and (arr[-1] == '.'): arr.pop()
    return arr

def insertValue(arr):
    if arr == []:
        arr.extend(['a', 'a', 'a'])
    return arr

def removeUpper15(arr):
    if len(arr) >= 16:
        result = arr[:15]
        if result[-1] == '.': result.pop()
        return result
    return arr

def extendString(arr):
    if len(arr) <= 2:
        while len(arr) < 3:
            arr.append(arr[-1])
    return arr