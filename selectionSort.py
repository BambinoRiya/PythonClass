class Solution: 
    def select(self, arr, i):
        # code here 
        min_index = i
        for index in range(i, len(arr)):
            if arr[min_index]>arr[i]:
                min_index=i
        return mind_index
    def selectionSort(self, arr,n):
        #code here
        for i in range(n):
            min_index = i
            for index in range(i, n):
                if arr[min_index]>arr[index]:
                    min_index=index
            arr[i], arr[min_index]=arr[min_index], arr[i]
          
