class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False

        highest_num = max(arr)
        highest_index = arr.index(highest_num)

        if highest_index == 0 or highest_index == len(arr) - 1:
            return False

        for i in range(0, highest_index):
            if arr[i] >= arr[i+1]:
                return False

        for j in range(highest_index, len(arr)-1):
            if arr[j] <= arr[j+1]:
                return False

        return True

  #time complexity O(n)
  #space complexity O(1)
