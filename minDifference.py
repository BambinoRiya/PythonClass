class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums = sorted(nums)
        left = 0
        n = len(nums)

        if n <= 3:
            return 0
        right = (n - 3) - 1
        diff = float('inf')

        while right < n:
            ans = nums[right]- nums[left]
            right +=1
            left +=1

            diff = min(diff,ans)

        return diff



        
