class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        from collections import defaultdict
        sudoku_checker = defaultdict(set)

        for i in range(9):
            for j in range(9):
                item = board[i][j]
                if item != ".":
                    row_pos = (i, -1)
                    col_pos = (-1, j)
                    if item in sudoku_checker[row_pos] or item in sudoku_checker[col_pos]:
                        return False

                    sudoku_checker[row_pos].add(item)
                    sudoku_checker[col_pos].add(item)

                    box_pos = (i // 3, j // 3)
                    if item in sudoku_checker[box_pos]:
                        return False
                    
                    sudoku_checker[box_pos].add(item)

        
        return True


        