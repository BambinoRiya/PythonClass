from collections import Counter
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <2:
            return 0

        arr = [True] * (n)
        arr[0] = False
        arr[1] = False
        

        for i in range(2,int((n)**0.5)+1):
            if arr[i] == True:
                for j in range(i**2, n,i):
                    arr[j] = False

        count = Counter(arr)
        
        return count[True]
        
