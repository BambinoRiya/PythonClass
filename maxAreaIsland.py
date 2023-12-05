class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def in_bound(i,j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
                return False
            return True

        def dfs(i, j):
            if not in_bound(i,j):
                return 0
            if grid[i][j] == "0": # water or visited
                return 0
            
            grid[i][j] = "0"
            return 1 + dfs(i+1, j) + dfs(i-1, j) + dfs(i, j+1) + dfs(i, j-1) 

        res = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                res = max(res, dfs(i,j))
        
        return res
