class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        res = 1
        if num == 1:
            return False
        for i in range(2, int(sqrt(num))+1):
            if num % i == 0:
                res+=i+num/i
        
        return res == num