from typing import List
import time


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        print('-' * 17)
        print_2d_array(matrix)
        print('-' * 17)
        print_2d_array(matrix)
        n = len(matrix)

        start = 0
        end = n-1
        while start < n // 2:
            for i in range(start, end):
                # rotate one layer
                tmp = matrix[i][start]
                matrix[i][start] = matrix[end][i]
                matrix[end][i] = matrix[n-1-i][end]
                matrix[n-1-i][end] = matrix[start][n-1-i]
                matrix[start][n-1-i] = tmp
                time.sleep(1)
                print('\033['+str(n)+'A', end='')
                print_2d_array(matrix)
            start += 1
            end -= 1


def print_2d_array(array):
    for row in array:
        print(' '.join('{:3}'.format(item) for item in row))


matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
Solution().rotate(matrix)
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Solution().rotate(matrix)
