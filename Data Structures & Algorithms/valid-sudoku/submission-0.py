class Solution:
   def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        sqrs = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                cur_cell = board[r][c]
                if cur_cell == '.':
                    continue
                
                if (
                    cur_cell in rows[r] or cur_cell in cols[c] or cur_cell in sqrs[r//3, c//3]
                ):
                    return False
                
                rows[r].add(cur_cell)
                cols[c].add(cur_cell)
                sqrs[r//3, c//3].add(cur_cell)
        
        return True