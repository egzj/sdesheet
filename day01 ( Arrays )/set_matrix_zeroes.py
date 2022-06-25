class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rowIndexes = []
        columnIndexes = []

        for i, x in enumerate(matrix):
            for j, y in enumerate(matrix[i]):
                if matrix[i][j] == 0:
                    if j not in columnIndexes:
                        columnIndexes.append(j)
                    if i not in rowIndexes:
                        rowIndexes.append(i)

        for ci in columnIndexes:
            # set entire column to 0 for matching columns
            for b in range(len(matrix)):
                matrix[b][ci] = 0

        for ri in rowIndexes:
            # set entire row to 0
            matrix[ri][:] = [0 for a in matrix[ri][:]]
