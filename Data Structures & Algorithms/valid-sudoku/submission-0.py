class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        from collections import defaultdict

        # Row col check
        seen_row_col = defaultdict(set)
        for i in range(9):
            for j in range(9):
                item = board[i][j]
                if item != ".":
                    if item in seen_row_col[(i, -1)] or item in seen_row_col[(-1, j)]:
                        return False
                    seen_row_col[(i, -1)].add(item)
                    seen_row_col[(-1, j)].add(item)

        # 3x3 box check
        seen_box = defaultdict(set)
        for i in range(9):
            for j in range(9):
                item = board[i][j]
                if item != ".":
                    row_pos = i // 3
                    col_pos = j // 3
                    if item in seen_box[(row_pos, col_pos)]:
                        return False
                    seen_box[(row_pos, col_pos)].add(item)
    
        return True
