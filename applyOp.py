class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        length = len(nums)
        newList = []

        for i in range(length - 1):
            if nums[i] == nums[i+1]:
                nums[i] = nums[i] * 2
                nums[i+1] = 0

        while 0 in nums:
            for x in nums:
                if x == 0:
                    newList.append(x)
                    nums.remove(x)

        nums.extend(newList)
        return nums

#Time complexity O(n**2)
      


