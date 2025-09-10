from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        left, right = 0, n-1
        top, bottom = 0, n-1
        num = 1

        while left < right and top < bottom:
            for j in range(left, right):
                matrix[top][j] = num
                num += 1
            for i in range(top, bottom):
                matrix[i][right] = num
                num += 1
            for j in range(right, left, -1):
                matrix[bottom][j] = num
                num += 1
            for i in range(bottom, top, -1):
                matrix[i][left] = num
                num += 1
            left += 1
            right -= 1
            top += 1
            bottom -= 1

        if left == right:
            for i in range(top, bottom+1):
                matrix[i][left] = num
                num += 1
        elif top == bottom:
            for j in range(left, right+1):
                matrix[top][j] = num
                num += 1

        return matrix


def print_2d_array(array):
    for row in array:
        print(' '.join('{:3}'.format(item) for item in row))


n = 3
print_2d_array(Solution().generateMatrix(n))
