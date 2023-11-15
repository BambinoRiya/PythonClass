class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        new_str = [letter for letter in s]
        count = 0
        for x in s:
            if x == letter:
                count+=1

        divider = count/ len(new_str)
        res = floor(divider * 100)

        return res

        
