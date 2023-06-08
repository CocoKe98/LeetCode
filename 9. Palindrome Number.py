class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        y = x
        cur = 0
        while x > 0 :
            cur = cur * 10 + x % 10
            x = x // 10
        return cur == y