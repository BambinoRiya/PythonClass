class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        outputList = []
        for i in range(len(nums)):
            counter = 0
            for j in range(len(nums)):
                if nums[i] > nums[j]:
                    counter +=1
                    
            outputList.append(counter)

        return outputList

#time complexity O(n**2)
#space complexity O(1)
