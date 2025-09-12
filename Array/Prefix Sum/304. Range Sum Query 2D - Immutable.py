from typing import List
from pprint import pprint


class NumMatrix:
    # https://labuladong.online/algo/data-structure/prefix-sum/#二维矩阵中的前缀和
    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        self.preSum = [[0] * (n + 1) for _ in range(m + 1)]

        # build 2D prefix sum
        # preSum[i][j] = 矩阵中 [0..i-1][0..j-1] 这个子矩阵的元素和
        # preSum 比原矩阵多一行一列（方便处理边界，类似一维前缀和）
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                self.preSum[i][j] = (
                    self.preSum[i - 1][j]
                    + self.preSum[i][j - 1]
                    - self.preSum[i - 1][j - 1]
                    + matrix[i - 1][j - 1]
                )
        pprint(matrix)
        pprint(self.preSum)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            self.preSum[row2 + 1][col2 + 1]
            - self.preSum[row1][col2 + 1]
            - self.preSum[row2 + 1][col1]
            + self.preSum[row1][col1]
        )


# Your NumMatrix object will be instantiated and called as such:
matrix = [
    [3, 0, 1, 4, 2],
    [5, 6, 3, 2, 1],
    [1, 2, 0, 1, 5],
    [4, 1, 0, 1, 7],
    [1, 0, 3, 0, 5],
]
obj = NumMatrix(matrix)
param_1 = obj.sumRegion(2, 1, 4, 3)
print(param_1)
