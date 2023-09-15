class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0,len(nums)
        nums.append(float("-inf"))
        while left <= right:
            mid = left+(right-left)//2
            if nums[mid] < nums[mid+1]:
                left = mid + 1
            elif nums[mid] < nums[mid -1]:
                right = mid - 1
            else:
                return mid
    #Time complexity : O(logn)
    #Space complexity : O(1)
