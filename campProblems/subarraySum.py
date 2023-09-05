class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        running_sum = 0
        prefix_dict = {0:1} #initializing a dictionary to store counts
        count = 0

        for i in range(len(nums)):
            running_sum += nums[i] #getting the prefix sum of each i
            comp = running_sum - k

            if comp in prefix_dict:
                count += prefix_dict[comp]

            if running_sum in prefix_dict:
                prefix_dict[running_sum] += 1
            else:
                prefix_dict[running_sum] = 1

        return count
       


        #time complexity : O(n)
        #space complexity : O(n)
