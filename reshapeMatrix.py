class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        row, col = len(mat), len(mat[0])
        if row * col != r*c: return mat

        newMat =[]
        currentRow =[]
        for i in range(row):
            for j in range(col):
                currentRow.append(mat[i][j])
                if len(currentRow) == c:
                    newMat.append(currentRow)
                    currentRow = []

        return newMat

  #Time complexity O(n**2)
  #Space complexity O(r*c)
