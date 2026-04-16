class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        if not grid:
            return -1
        
        num_minutes = 0
        fresh_oranges = 0
        rotten_q = collections.deque()
        n_rows, n_cols = len(grid), len(grid[0])

        for row in range(n_rows):
            for col in range(n_cols):
                if grid[row][col] == 1:
                    fresh_oranges += 1
                if grid[row][col] == 2:
                    rotten_q.append((row, col))
        
        new_dirs = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        
        while rotten_q and fresh_oranges > 0:
            for _ in range(len(rotten_q)):
                row, col = rotten_q.popleft()
                for dr, dc in new_dirs:
                    nr, nc = row + dr, col + dc
                    if (0 <= nr < n_rows and 
                        0 <= nc < n_cols and 
                        grid[nr][nc] == 1):
                        grid[nr][nc] = 2
                        rotten_q.append((nr, nc))
                        fresh_oranges -= 1
            num_minutes += 1
        
        return num_minutes if fresh_oranges == 0 else -1 
                    

        





        