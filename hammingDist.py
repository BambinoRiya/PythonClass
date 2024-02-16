class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        num = x ^ y
        count = 0
        for i in range(num.bit_length()):
            if num & 1 == 1:
                count +=1
            num >>= 1

        return count


        Time complexity: O(n)
        Space complexity: O(n)
