class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapify(stones)

        while len(stones) > 1:
            num1 = heappop(stones)
            num2 = heappop(stones)

            if not (num1==num2):
                value = abs(num1) - abs(num2)
                heappush(stones,-value)

        if len(stones) >=1:
            return abs(stones[0])
        else:
            return 0        
