class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        for i in range(0, (len(nums)+1)):
            if i not in nums:
                return i

        #time complexity is O(n) and space complexity is O(1)



