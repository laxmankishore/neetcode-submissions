class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def dfs(grid, row, col, seen):
            if row < 0 or col < 0 or (row == rows) or (col == cols) or ((row, col) in seen) or grid[row][col] == 1: 
                return 0
    
            if row == rows - 1 and col == cols - 1 :
                return 1
            
            seen.add((row, col))
            count = 0
            count += dfs(grid, row + 1, col, seen)
            count += dfs(grid, row - 1, col, seen)
            count += dfs(grid, row, col + 1, seen)
            count += dfs(grid, row, col - 1, seen)

            seen.remove((row, col))
            return count

        return dfs(grid, 0, 0, set())
            






        

        