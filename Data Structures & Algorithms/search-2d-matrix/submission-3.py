class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        ## think like a bin search 
        length = ROWS * COLS
        left, right = 0, length - 1

        while left <= right:
            mid = (left + right)//2
            mid_row = mid // COLS
            mid_col = mid % COLS
            mid_num = matrix[mid_row][mid_col]

            if mid_num == target: return True
            if mid_num > target : right = mid - 1
            else : left = mid + 1

        return False

        