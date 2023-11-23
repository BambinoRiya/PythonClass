from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        len_s, len_p = len(s), len(p)
        res = []
        
        p_count = Counter(p)
        window_count = Counter(s[:len_p])
        
        if window_count == p_count:
            res.append(0)
      
        for i in range(len_p, len_s):
            window_count[s[i - len_p]] -= 1
            if window_count[s[i - len_p]] == 0:
                del window_count[s[i - len_p]]
            window_count[s[i]] += 1

            
            if window_count == p_count:
                res.append(i - len_p + 1)

        return res
