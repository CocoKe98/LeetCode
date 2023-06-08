class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        for i in range(len(nums)):
            b = target - nums[i]
            for j in range(1, len(nums) - i):
                if nums[i+j] == b:
                    res.append(i)
                    res.append(j+i)
        return res