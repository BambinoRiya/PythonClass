class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        i = 0
        n = len(nums)

        while i < n:
            correct_pos = nums[i] - 1
            if nums[i] != nums[i] + 1 and nums[correct_pos] != nums[i]:
                nums[correct_pos], nums[i] = nums[i], nums[correct_pos]
            else:
                i+=1
        
        dupes = []
        for i in range(len(nums)):
            if nums[i] -1 != i:
                dupes.append(nums[i])

        return dupes
        
