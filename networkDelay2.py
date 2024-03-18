class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        mat = [[float('inf')]*n for _ in range(n)]

        for src, dest, time in times:
            mat[src-1][dest-1] = time

        for i in range(n):
            mat[i][i] = 0

        for m in range(n):
            for i in range(n):
                for j in range(n):
                    mat[i][j] = min(mat[i][j], mat[i][m]+ mat[m][j])
       
        if type(max(mat[k-1])) is float: 
            return -1
        else:
            return  max(mat[k-1])
        
