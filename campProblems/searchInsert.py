class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect.bisect_left(nums,target)
        #time complexity : O(logn)
        #space complexity : O(1)
        
