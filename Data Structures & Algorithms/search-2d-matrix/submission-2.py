class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        N = len(matrix)
        M = len(matrix[0])

        l, r = 0, N*M-1
        while l <= r:
            mid = l + (r - l) // 2
            i = mid // M
            j = mid % M
            if matrix[i][j] == target:
                return True
            if matrix[i][j] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False