class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        new_set = set(nums)  #creates new var that is a set, because there will be no duplicates

        if len(new_set) != len(nums):
            return True  # Lengths are different, so values must be different

        for i in range(len(nums)):
            if nums[i] in new_set:
                return False  # Value exists in both set and list

        return True  # No common values found
