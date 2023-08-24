class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n  # In case k is greater than the length of the array
        extracted_elements = nums[-k:]
        del nums[-k:]
        nums[:0] = extracted_elements
        return nums
