from itertools import permutations
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [n for n in range(1,n+1)]
        perm = sorted(list(permutations(nums)))
        # print(perm)
        ans = ""
        for letter in perm[k-1]: 
            ans += (str(letter))


        return (ans)
        
