class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        sortedPile = sorted(piles)
        size = len(sortedPile)
        j = size - 1
        answer =0

        for i in range(size//3):
            j -=1
            answer +=sortedPile[j]
            j -=1
        return answer

        #time :  O(nlogn)
        #space: O(1)
