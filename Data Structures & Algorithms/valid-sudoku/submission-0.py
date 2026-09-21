class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        subgrids = defaultdict(dict)
        columns = defaultdict(dict)
        for i, row in enumerate(board):
            row_items = dict()
            for j, el in enumerate(row):
                if el == ".": continue
                if el in row_items:
                    return False
                if el in columns[j]:
                    return False
                row_items[el] = True
                columns[j][el] = True

                if el in subgrids[(i // 3, j // 3)]:
                    return False
                subgrids[(i // 3, j // 3)][el] = True

        
        return True

# col = j // 3
# row = i // 3
# [["0","1","2","3","4","5","6","7","8"],
#  ["0","1","2","3","4","5","6","7","8"],
#  ["0","1","2","3","4","5","6","7","8"],
#  ["0","1","2","3","4","5","6","7","8"],
#  ["0","1","2","3","4","5","6","7","8"],
#  ["0","1","2","3","4","5","6","7","8"],
#  ["0","1","2","3","4","5","6","7","8"],
#  ["0","1","2","3","4","5","6","7","8"],
#  ["0","1","2","3","4","5","6","7","8"]]