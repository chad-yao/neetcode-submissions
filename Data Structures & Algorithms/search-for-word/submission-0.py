class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        rows = len(board)
        cols = len(board[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        ans = False
        
        def dfs(row, col, idx, visited):
            nonlocal ans

            if row < 0 or row >= rows:
                return
            if col < 0 or col >= cols:
                return
            
            if idx >= len(word):
                return

            if visited[row][col]:
                return

            if board[row][col] != word[idx]:
                return

            if idx == len(word) - 1:
                ans = True
            
            directions = [
                [-1, 0],
                [1, 0],
                [0, -1],
                [0, 1],
            ]
            visited[row][col] = True
            for dx, dy in directions:
                    dfs(row + dx, col + dy, idx + 1, visited)
            visited[row][col] = False

        for i in range(rows):
            for j in range(cols):
                dfs(i, j, 0, visited)
                if ans:
                    break
            if ans:
                break

        return ans