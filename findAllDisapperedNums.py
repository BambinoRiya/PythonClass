class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        n = len(nums)
        i = 0

        while i < n:
            correct_pos = nums[i] - 1
            if nums[i] != nums[i] + 1 and nums[correct_pos] != nums[i]:
                nums[correct_pos],nums[i] = nums[i],nums[correct_pos]
            else:
                i+=1
        
        res = [i+1 for i in range(n) if nums[i] != i+1]

        return res
