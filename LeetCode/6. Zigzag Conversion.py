class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        result = [""]*(numRows+1)
        floor = 2
        direct = 1
        
        result[1] += s[0]
        
        for idx in range(1, len(s)):
            result[floor] += s[idx]
            
            if floor == 1:
                direct = 1
            elif floor == numRows:
                direct = -1
            floor += direct
    
        
        
        return "".join(result)