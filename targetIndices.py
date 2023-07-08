class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        targetIndices = []
        sortedNums = sorted(nums)
    
        for i in range(len(sortedNums)):
            if sortedNums[i] == target:
                targetIndices.append(i)
    
        return targetIndices
