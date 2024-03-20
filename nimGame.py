class Solution:
    def canWinNim(self, n: int) -> bool:
        if n == 1 or n == 2:
            return True
        elif (n/2 )% 2 ==0:
            return False
        else:
            return True
        
