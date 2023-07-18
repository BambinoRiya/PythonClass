class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = sorted(set(nums))
        print(nums)
        return len(nums)


#time complexity: O(1)
#space : O(1)
