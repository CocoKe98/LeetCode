class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = 0
        c = 0
        for i in nums:
            if c == 0:
                d = i

            if d != i:
                c -= 1
            else:
                c += 1

        return d