class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        m = len(matrix)
        n = len(matrix[0])
        left, right = 0, n-1
        top, bottom = 0, m-1

        while left < right and top < bottom:
            for j in range(left,right):
                res.append(matrix[top][j])
            for i in range(top,bottom):
                res.append(matrix[i][right])
            for j in range(right,left,-1):
                res.append(matrix[bottom][j])
            for i in range(bottom,top,-1):
                res.append(matrix[i][left])
            left   += 1
            right  -= 1
            top    += 1
            bottom -= 1

        if left == right:
            for i in range(top,bottom+1):
                res.append(matrix[i][left])
        elif top == bottom:
            for j in range(left,right+1):
                res.append(matrix[top][j])

        return res

"""
m x n, m = 4, n = 5
=========================================
        left            right
          ↓               ↓
   top →  1   2   3   4   5
          6   7   8   9  10
         11  12  13  14  15
bottom → 16  17  18  19  20
=========================================
pattern
+-------------------+ +-----+
|         →         | |     |
+-------------------+ |     |
+-----+               |  ↓  |
|     |               |     |
|     |               |     |
|  ↑  |               +-----+
|     | +-------------------+
|     | |         ←         |
+-----+ +-------------------+

j = [left →  right) matrix[ top  ][  j  ]
i = [top  → bottom) matrix[  i   ][right]
j = (left ←  right] matrix[bottom][  j  ]
i = (top  ← bottom] matrix[  i   ][left ]
=========================================
"""

solution = Solution()
matrix = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
print(solution.spiralOrder(matrix))
