def solution(babbling):
    answer = 0
    words = ["aya", "ye", "woo", "ma"]
    for sentence in babbling:
        result = replaceAll(sentence, words)
        answer += result
    return answer

def replaceAll(string, words):    
    for word in words:
        if word * 2 in string: return False
        string = " ".join(string.split(word))
    
    if string.strip() == "": return True
    return False
    