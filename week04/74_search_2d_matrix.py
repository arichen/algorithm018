class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        row, col = len(matrix), len(matrix[0])
        low, high = 0, row * col - 1
        while low <= high:
            mid = low + (high - low) // 2
            r, c = (mid // col), (mid % col)

            if matrix[r][c] == target:
                return True
            if matrix[r][c] < target:
                low = mid + 1
            else:
                high = mid - 1
        return False