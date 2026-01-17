class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[0])):
                if target==matrix[i][j]:
                    return True
        return False