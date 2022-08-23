class Solution:
    def reverse(self, x: int) -> int:
        maxvalue = pow(2,31)
        num = str(x)
        
        if num[0] == "-":
            value = int(num[len(num)-1:0:-1])
            value = -value
        else:
            num = num[len(num)-1:0:-1] + num[0]
            value = int(num)
        
        if value > maxvalue or value < -maxvalue:
            return 0
        else:
            return value
            