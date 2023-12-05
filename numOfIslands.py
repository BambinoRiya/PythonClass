class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        def in_bound(i,j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return False
            return True

        def dfs(i, j):
            if not in_bound(i,j):
                return
            if grid[i][j] == "0": # water or visited
                return
            
            grid[i][j] = "0"
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    dfs(i,j)
                    count += 1
        
        return count
        
            
