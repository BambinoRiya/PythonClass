from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        occurrences = Counter(nums)
        list_size = len(nums) 
        expression = list_size / 2
        
        for element, count in occurrences.items():
            if count > expression:
                return element

        return None

