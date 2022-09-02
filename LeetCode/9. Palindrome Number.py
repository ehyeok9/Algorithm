class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = str(x)
        print(num)
        middle = len(num)//2
        
        for i in range(middle):
            if num[i] == num[len(num) - i -1]:
                continue
            else:
                return False
        return True