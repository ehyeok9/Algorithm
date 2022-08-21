class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) == 0:
            return 0
        length = []
        
        for i in range(len(s)):
            word = 1
            alphabet = []
            alphabet.append(s[i])
            
            for j in range(i+1, len(s)):
                if s[j] in alphabet:
                    break
                alphabet.append(s[j])
                word += 1
                
            length.append(word)
            
        
        return max(length)