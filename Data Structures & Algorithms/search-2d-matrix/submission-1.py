class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix)-1
        while l < r:
            mid = l + (r - l) // 2
            if matrix[mid][-1] == target:
                return True
            if matrix[mid][-1] < target:
                l = mid + 1
            else:
                r = mid
        
        row = l
        l, r = 0, len(matrix[row]) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if matrix[row][mid] == target:
                return True
            if matrix[row][mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False