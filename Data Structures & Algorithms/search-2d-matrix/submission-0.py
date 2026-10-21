class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binSearch(arr, target):
            l = 0
            r = len(arr) - 1
            while l <= r:
                mid = l + (r - l) // 2
                if arr[mid] == target:
                    return mid

                elif arr[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            
            return -1

        row = 0
        while row < len(matrix):
            if matrix[row][-1] == target: return True
            if matrix[row][-1] > target:
                break
            row += 1
        
        if row == len(matrix):
            return False

        return binSearch(matrix[row], target) != -1