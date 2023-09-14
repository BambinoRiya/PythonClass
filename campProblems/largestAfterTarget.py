class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left, right = 0, len(letters)

        if ord(letters[-1]) <= ord(target):
            return letters[0]
    
        while left <= right :
            mid = left + (right - left) // 2
            if ord(target) < ord(letters[mid]):
                right = mid -1
            # elif ord(target) > ord(letters[mid]):
            #     left = mid + 1
            else:
                left = mid + 1
        
        return letters[left]
