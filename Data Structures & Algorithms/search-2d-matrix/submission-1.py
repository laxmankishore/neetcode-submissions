class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        T = rows * cols 

        left, right = 0, T - 1

        while left <= right:
            mid = (left + right) // 2
            mid_row = mid // cols
            mid_col = mid % cols
            if matrix[mid_row][mid_col] == target:
                return True
            elif target > matrix[mid_row][mid_col] :
                left += 1
            else :
                right -= 1
        return False
            

        