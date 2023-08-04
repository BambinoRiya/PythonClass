class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        C = []
        tmp = {}
        if A[0] == B[0]:
            C.append(1)
        else:
            C.append(0)
        tmp[A[0]] = 1
        tmp[B[0]] = 1
        for i in range(1,len(A)):
            tmp[A[i]] = 1
            tmp[B[i]] = 1
            C.append((i+1)*2 - len(tmp)) 
        return C
        
