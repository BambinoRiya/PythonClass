class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        test = nums[0]
        result.append(test)
        for i in range(1, len(nums)):
            test = test + nums[i]
            result.append(test)

        return result

  # time complexity == O(n) 
