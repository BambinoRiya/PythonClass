class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1, -1]
        else:
            return (bisect_left(nums,target), bisect_right(nums,target)-1)

        # left, right = 0, len(nums) - 1
        # end = 1
        # position = len(nums)
        # if target not in nums:
        #     return [-1, -1]

        # while left <= right:
        #     mid = left + (right - left)//2
        #     if target < nums[mid]:
        #         right = mid - 1 
                

        #still to come up with better and more authentic and less easy solution
      #time complexity : O(logn)
