class Solution:
    def findMin(self, nums: List[int]) -> int:
        left,right= 0,len(nums)-1
        ans = nums[0]
        while left<= right:
            if nums[left] < nums[right]:
                ans=min(ans,nums[left])
                break
            mid = left+ (right-left)//2
            ans = min(ans, nums[mid])
            if nums[mid] >= nums[left]:
                left = mid +1
            else:
                right = mid - 1
        return ans
