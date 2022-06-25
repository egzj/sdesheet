class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rows = []
        for i in range(numRows):  # i = 2
            row = []
            for j in range(i + 1):
                # set first element to 1
                if j == 0:
                    row.append(1)
                # set last element to 1
                elif j == i:
                    row.append(1)
                else:
                    # look for pev row to get sum
                    sum = rows[i - 1][j - 1] + rows[i - 1][j]
                    row.append(sum)

            rows.append(row)
        return rows


# Success
# Details
# Runtime: 30 ms, faster than 94.43% of Python3 online submissions for Pascal's Triangle.
# Memory Usage: 13.8 MB, less than 65.77% of Python3 online submissions for Pascal's Triangle.
