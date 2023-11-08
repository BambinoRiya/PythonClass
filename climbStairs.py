class Solution:
    @cache
    def climbStairs(self, n: int) -> int:
        #base case
        if n == 0:
            return 1
        if n < 0:
            return 0
        return self.climbStairs(n-2) + self.climbStairs(n-1)
