class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        a = len(word1)  #"abc" 3
        b = len(word2)  #"pqry" 4

        newString = ""

        for i in range(max(a,b)): #0,4
            if i < a :              #yes
                newString = newString + word1[i] #abc
            if i < b:
                newString = newString + word2[i] #pqr

        return newString
