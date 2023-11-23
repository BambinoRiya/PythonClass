class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        right = k
        curr_sum = sum(nums[left:right])
        res=[curr_sum/k]

        while right < len(nums):
            curr_sum = curr_sum - nums[left] + nums[right]
            res.append(curr_sum/k)
            left +=1
            right +=1

        return max(res)
