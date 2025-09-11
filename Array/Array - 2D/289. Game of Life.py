from typing import List

class Solution(object):
    # https://www.cnblogs.com/lightwindy/p/8661499.html
    # Bit Manipulation
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])

        for i in range(m):
            for j in range(n):
                count = 0
                # Count live cells in 3x3 block.
                for I in range(max(i-1, 0), min(i+2, m)):
                    for J in range(max(j-1, 0), min(j+2, n)):
                        count += board[I][J] & 1

                # if (count == 4 && board[i][j]) means:
                #     Any live cell with three live neighbors lives.
                # if (count == 3) means:
                #     Any live cell with two live neighbors.
                #     Any dead cell with exactly three live neighbors lives.
                if (count == 4 and board[i][j]) or count == 3:
                    board[i][j] |= 2  # Mark as live.

        for i in range(m):
            for j in range(n):
                board[i][j] >>= 1  # Update to the next state.


    '''
    原地更新法
     0:「原本死, 现在死」0 -> 0
     1:「原本活, 现在活」1 -> 1
    -1:「原本活, 现在死」1 -> 0
     2:「原本死, 现在活」0 -> 1
    这样统计邻居时用 abs() 就能看到“原本状态”，避免干扰。
    最后再统一收尾，得到最终状态。
    '''
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])

        def count_live_neighbors(x, y):
            cnt = 0
            for i in range(x-1, x+2):
                for j in range(y-1, y+2):
                    if (i == x and j == y) or i < 0 or i >= m or j < 0 or j >= n:
                        continue
                    if abs(board[i][j]) == 1:
                        cnt += 1
            return cnt

        # Step 1: apply rules with temporary markers
        for i in range(m):
            for j in range(n):
                live_neighbors = count_live_neighbors(i, j)
                if board[i][j] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[i][j] = -1  # live -> dead
                if board[i][j] == 0 and live_neighbors == 3:
                    board[i][j] = 2   # dead -> live

        # Step 2: finalize the board
        for i in range(m):
            for j in range(n):
                if board[i][j] > 0:
                    board[i][j] = 1
                else:
                    board[i][j] = 0


solution = Solution()
board = [
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
print(solution.gameOfLife(board))