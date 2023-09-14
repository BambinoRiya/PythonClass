# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left,right = 1,n
        while left <= right:
            num = left + (right-left)//2 #getting middle value

            if guess(num) == -1:right = num - 1   
            elif guess(num) == 1: left = num + 1
            else: return num
        
#Time complexity : O(logn)**
#Space complexity : O(n)**
