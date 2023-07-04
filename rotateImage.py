class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # Reverse each row
        for i in range(len(matrix)):
            for j in range(len(matrix) // 2):
                matrix[i][j], matrix[i][len(matrix) - j - 1] = matrix[i][len(matrix) - j - 1], matrix[i][j]
        
        return matrix
  
    def rotate(self, matrix):
        n = len(matrix)
        
        for i in range((n + 1) // 2):
            for j in range(n // 2):
                # Start 4-way swaps
                # temp = bottom left
                temp = matrix[n - 1 - j][i]
                
                # bottom left = bottom right
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - j - 1]
                
                # bottom right = top right
                matrix[n - 1 - i][n - j - 1] = matrix[j][n - 1 - i]
                
                # top right = top left
                matrix[j][n - 1 - i] = matrix[i][j]
                
                # top left = temp
                matrix[i][j] = temp
#time complexity O(n)
#space complexity O(1)
