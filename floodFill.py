class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        curr = image[sr][sc]
        def in_bound(i,j):
            if i < 0 or i == len(image) or j < 0 or j == len(image[0]):
                return False
            return True
            
        def dfs(i, j):
            if not in_bound(i,j):
                return
            if image[i][j] == color or image[i][j] != curr:
                return

            image[i][j] = color
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
        
        dfs(sr,sc)
        
        return image
        
