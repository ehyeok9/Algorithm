wordtonum = {
        "zero" : "0",
        "one" : "1",
        "two" : "2",
        "three" : "3",
        "four" : "4",
        "five" : "5",
        "six" : "6",
        "seven" : "7",
        "eight" : "8",
        "nine" : "9",
    }

def solution(s):
    answer = []
    
    string = ""
    for i in range(len(s)):
        if "a" <= s[i] <= "z":
            string += s[i]
            if string in wordtonum.keys():
                answer.append(wordtonum[string])
                string = ""
        else:
            if string != "":
                answer.append(wordtonum[string])
                string = ""
            answer.append(s[i])
    
    
    return int("".join(answer))