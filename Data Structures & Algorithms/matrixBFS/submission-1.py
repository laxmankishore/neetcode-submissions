from collections import deque
class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        que = deque()
        seen = set()
        que.append((0,0))
        seen.add((0,0))

        length = 0
        while que:
            for _ in range(len(que)):
                row, col = que.popleft()
                if row == ROWS - 1 and col == COLS - 1:
                    return length

                for nr, nc in [(row, col + 1), (row, col - 1), (row + 1, col), (row - 1, col)]:
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 0 and (nr, nc) not in seen:
                        que.append((nr, nc))
                        seen.add((nr, nc))
            length += 1
        
        return -1 






        


        