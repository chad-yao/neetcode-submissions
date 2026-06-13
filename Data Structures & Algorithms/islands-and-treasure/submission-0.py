class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647

        row = len(grid)
        col = len(grid[0])

        def dfs(i, j, depth):
            if i < 0 or i >= row:
                return
            if j < 0 or j >= col:
                return
            if grid[i][j] < depth:
                return
            
            # first visit
            if grid[i][j] == INF:
                grid[i][j] = depth
            # if short path exists
            elif grid[i][j] > 0:
                grid[i][j] = depth if depth < grid[i][j] else grid[i][j]

            dfs(i,j+1,depth+1)
            dfs(i,j-1,depth+1)
            dfs(i+1,j,depth+1)
            dfs(i-1,j,depth+1)

        
        for i in range(row):
            for j in range(col):
                # found treasure
                if grid[i][j] == 0:
                    # start dfs
                    dfs(i,j,0)
        
                
        