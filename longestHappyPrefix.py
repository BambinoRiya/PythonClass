class Solution:
    def longestPrefix(self, s: str) -> str:
        mod = 10**9 + 7
        left = 0
        right = len(s) - 1
        prefix = (ord(s[0]) - ord('a') + 1)%mod
        suffix = (ord(s[-1]) -ord('a') + 1)%mod
       
        biggest = 0
        prime = 31
        while left < len(s)-1 and right > 0:
            if prefix == suffix:
                biggest = max(biggest,left+1)

            left += 1
            right -= 1
            prefix *= 31
            prefix += ((ord(s[left]) - ord('a')) + 1)
            prefix %= mod
        
            suffix += ((ord(s[right]) - ord('a') + 1) * prime)
            prime *= 31
            prime %= mod
            suffix %= mod
           
        if biggest == 0:
            return ''
        
        return s[:(biggest)]
        
