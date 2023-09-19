class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left,right= 1,max(piles)
        while left< right:
            mid = left + (right-left)//2
            total = sum([math.ceil(pile/mid) for pile in piles])
            if h < total:
                left = mid + 1
            else:
                right = mid
        return left
        
