from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        occurrences = Counter(nums)
        list_size = len(nums) 
        expression = list_size / 3
        
        result = []
        for element, count in occurrences.items():
            if count > expression:
                result.append(element)

        return result
