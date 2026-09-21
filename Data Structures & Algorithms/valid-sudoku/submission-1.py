class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(dict)
        columns = defaultdict(dict)
        grids = defaultdict(dict)

        for row, line in enumerate(board):
            for column, el in enumerate(line):
                if el == ".": continue

                grid = row // 3 * 10 + column // 3

                if el in rows[row] or el in columns[column] or el in grids[grid]:
                    return False

                rows[row][el] = True
                columns[column][el] = True
                grids[grid][el] = True

        
        return True