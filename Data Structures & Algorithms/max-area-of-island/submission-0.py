class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        
        def dfs(i,j):
            if i<0 or i>=row:
                return 0
            if j<0 or j>=col:
                return 0
            if grid[i][j] == 0:
                return 0
            
            grid[i][j] = 0

            up = dfs(i,j+1)
            down = dfs(i,j-1)
            right = dfs(i+1,j)
            left = dfs(i-1,j)

            return 1 + up + down + right + left


        ans = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    value = dfs(i,j)
                    ans = value if value >= ans else ans

        return ans
