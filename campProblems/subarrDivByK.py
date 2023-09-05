class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        running_sum = 0
        prefix = {0:1}
        count = 0

        for i in range(len(nums)):
            running_sum += nums[i]
            mod = running_sum % k

            if mod in prefix:
                count += prefix[mod]
             
            prefix[mod] = prefix.get(mod, 0) + 1

        return count

        # time complexity : O(n)
        # space complexity : O(n)


        
            

        
