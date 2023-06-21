class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        return sum(cost) - sum(sorted(cost, reverse=True)[2::3])
        