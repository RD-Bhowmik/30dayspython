class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        n = len(nums)

        max_diff = 0 

        for i in range(n):
            j = (i+1) % n 
            diff = abs(nums[i] - nums[j])
            max_diff = max(max_diff, diff)

        return max_diff