class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        def isBound(i,j,n):
            if 0 <= i < n and 0 <= j < n:
                return True
            return False

        if grid[0][0] == 1:
            return -1
        N = len(grid)
        queue = deque()
        queue.append((0,0,1))
        visited = set()
        visited.add((0,0))
        directions = ((1,0),(0,1),(-1,0),(0,-1),(-1,-1),(-1,1),(1,-1),(1,1))

        while queue:
            r,c,level = queue.popleft()

            if (r,c) == (N-1,N-1):
                return level

            for (x,y) in directions:
                new_r = x + r
                new_c = c + y

                if not isBound(new_r,new_c,N)or grid[new_r][new_c] == 1 or (new_r,new_c) in visited:
                    continue

                visited.add((new_r,new_c))
                queue.append((new_r,new_c,level+1))    

        return -1  
