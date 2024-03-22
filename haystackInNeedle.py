class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(needle)

        if m > len(haystack):
            return -1

        for i in range(len(haystack)):
            if needle == haystack[i:i+m]:
                return i
                continue
            
        return -1

#Robin Karp algorithm to be done by Sunday
        
