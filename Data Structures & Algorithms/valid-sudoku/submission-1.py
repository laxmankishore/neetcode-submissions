class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowset = set()
        colset = set()
        boxset = set()

        rows, cols = len(board), len(board[0])
        for row in range(rows): 
            for col in range(cols):
                if board[row][col] == ".":
                    continue
                if board[row][col] in rowset:
                    return False
                rowset.add(board[row][col])
            rowset.clear()
        
        for col in range(cols):
            for row in range(rows):
                if board[row][col] == ".":
                    continue
                if board[row][col] in colset:
                    return False
                colset.add(board[row][col])
            colset.clear()

        for box in range(9):
            for i in range(3):
                for j in range(3):
                    row = (box//3) * 3 + i
                    col = (box%3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in boxset:
                        return False
                    boxset.add(board[row][col])
            boxset.clear()
        
        return True
       