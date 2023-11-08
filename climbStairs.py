class Solution:
    @cache
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return n
        elif n == 1:
            return n
        elif n == 2:
            return n
        return self.climbStairs(n-2) + self.climbStairs(n-1)
        
