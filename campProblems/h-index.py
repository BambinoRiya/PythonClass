class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left,right = 0, len(citations) - 1
        # length = 0
        while left<= right:
            mid = left + (right-left) //2
            if citations[mid] > (len(citations)-mid):
                right = mid-1
            elif citations[mid] < (len(citations)-mid):
                left = mid + 1
            else:
                return len(citations) - mid
        return len(citations) - left

