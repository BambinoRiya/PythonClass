class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        total = 0
        min_len = float("inf")

        for right in range(len(nums)):
            total += nums[right]
            while total >= target:
                min_len = min(right-left + 1, min_len)
                total -=nums[left]
                left +=1

        if min_len == float("inf"):
            return 0
        else:
            return min_len

        
