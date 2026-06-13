class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # scan all rotten bananas
        q = deque()

        row = len(grid)
        col = len(grid[0])

        bananas_left = 0
        # add all rotten bananas into the queue
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    bananas_left += 1
                elif grid[i][j] == 2:
                    q.append((i,j))
        if bananas_left == 0:
            return 0
        time_step = 0
        while len(q) > 0:
            q_len = len(q)
            time_step += 1
            for _ in range(q_len):
                i, j = q.popleft()

                directions = [[-1,0],[1,0],[0,-1],[0,1]]
                for d in directions:
                    new_i = i+d[0]
                    new_j = j+d[1]
                    
                    if 0 <= new_i < row and 0 <= new_j < col:
                        # print(new_i, new_j)
                        if grid[new_i][new_j] == 1:
                            bananas_left -= 1
                            grid[new_i][new_j] = 2
                            q.append((new_i, new_j))

        if bananas_left > 0:
            return -1
        
        return time_step - 1

