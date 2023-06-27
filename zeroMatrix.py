class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])
        ZeroRows = set()
        ZeroCols = set()

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    ZeroRows.add(i)
                    ZeroCols.add(j)
                    
        for row_idx in range(row):
            for col_idx in ZeroCols:
                matrix[row_idx][col_idx] = 0
                
        for col_idx in range(col):
            for row_idx in ZeroRows:
                matrix[row_idx][col_idx] = 0

        return matrix

  #Time complexity O(n^2)
  #space complexity O(1)
