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

#Robin Karp algorithm 

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        def transform(word):
            n = len(word)
            curr = 0
            for i in range(len(word)):
                curr += ((ord(word[i]) - ord('a')+ 1) * (26**(n-i)))

            return curr

        ans = transform(needle)

        left = 0
        right = len(needle) - 1

        pre = transform(haystack[0:len(needle)])

        while right < (len(haystack))-1:
            if pre == ans:
                return left
            else:
                left +=1
                right+=1
                pre = (26*(pre - ((ord(haystack[left-1]) - ord('a') + 1) * (26**(len(needle)-1))))) + (ord(haystack[right]) - ord('a') + 1)
                #precompute

        if pre == ans:
            return left
        else:
        
            return -1
        
        
