class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        reversed_numbers = []
        
        for num in nums:
            num = str(num)[::-1]
            reversed_numbers.append(int(num))
        
        nums.extend(reversed_numbers)
        count = len(set(nums))

        return count

        #time complexity : O(n)
        #space complexity : O(1)
