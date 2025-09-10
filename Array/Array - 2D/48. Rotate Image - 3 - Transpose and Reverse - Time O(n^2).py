from typing import List
import time


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        
        # Step 1: transpose across the main diagonal
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2: reverse each row
        for row in matrix:
            i, j = 0, len(row)-1
            while i < j:
                row[i], row[j] = row[j], row[i]
                i += 1
                j -= 1


def print_2d_array(array):
    for row in array:
        print(' '.join('{:3}'.format(item) for item in row))


start_time = time.time()

matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]

print_2d_array(matrix)

Solution().rotate(matrix)

print('-' * 17)
print_2d_array(matrix)

print("--- %s seconds ---" % (time.time() - start_time))
