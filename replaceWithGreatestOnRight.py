class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        n = len(arr)
        maximum = -1

        for i in range(n-1, -1, -1):
            current = arr[i]
            arr[i] = maximum
            maximum = max(maximum, current)

        return arr

  #time complexity O(N)
  #Space O(1)
