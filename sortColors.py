class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        max_num = max(nums)
        temp_result = [0] * (max_num + 1) 

        for num in nums:
            temp_result[num] += 1  
            
        index = 0
        for num in range(len(temp_result)):
            count = temp_result[num]
            while count > 0:
                nums[index] = num
                index += 1
                count -= 1
#time complexity O(n)
#space complexity O(1)
