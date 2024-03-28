from collections import defaultdict
class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        target = total % p

        if target == 0:
            return 0
        
        min_length = len(nums)
        prev = defaultdict(int)
        curr_sum = 0
        prev[0] = -1

        for i in range(len(nums)):
            curr_sum += nums[i]
            comp = curr_sum % p
            prev[comp] = i
            ans = (curr_sum-target)%p

            if ans in prev:
                min_length = min(min_length, i-prev[ans])
        print(prev)
        return min_length if min_length < len(nums) else -1
        


            

            
