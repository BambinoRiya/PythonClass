class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res_str = ""
        first = 0
        second = 0
        
        while first < len(word1) and second < len(word2):
            res_str +=word1[first]
            res_str +=word2[second]
            first +=1
            second +=1
        
        while first < len(word1):
            res_str +=word1[first]
            first +=1
        while second < len(word2):
            res_str +=word2[second]
            second +=1

        return res_str 
        
