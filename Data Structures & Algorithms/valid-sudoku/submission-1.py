class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        from collections import defaultdict

        # Row col check
        seen_row_col = defaultdict(set)
        seen_box = defaultdict(set)
        for i in range(9):
            for j in range(9):
                item = board[i][j]
                if item != ".":
                    # Check row and col
                    if item in seen_row_col[(i, -1)] or item in seen_row_col[(-1, j)]:
                        return False
                    seen_row_col[(i, -1)].add(item)
                    seen_row_col[(-1, j)].add(item)


                    # Check box
                    row_pos = i // 3
                    col_pos = j // 3
                    if item in seen_box[(row_pos, col_pos)]:
                        return False
                    seen_box[(row_pos, col_pos)].add(item)
                    
    
        return True
