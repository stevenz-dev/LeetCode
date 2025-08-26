from typing import List
from collections import deque


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        target = [[1, 2, 3], [4, 5, 0]]
        m, n = len(board), len(board[0])
        zero_pos = self.findZero(board, m, n)
        q = deque([(board, zero_pos)])
        visited = {str(board)}
        moves = 0
        dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # left, right, up, down
        # print(q, visited, zero_pos)

        while q:
            for i in range(len(q)):
                board, zero_pos = q.popleft()
                # print(f"board: {board}, zero_pos: {zero_pos}")

                if board == target:
                    return moves

                for dir in dirs:
                    i, j = zero_pos[0], zero_pos[1]
                    new_i, new_j = i + dir[0], j + dir[1]
                    new_zero_pos = (new_i, new_j)
                    # print(new_zero_pos)
                    if 0 <= new_i < m and 0 <= new_j < n:
                        new_board = [row[:] for row in board]
                        new_board[i][j], new_board[new_i][new_j] = new_board[new_i][new_j], new_board[i][j]
                        # print(board, new_board)
                        if str(new_board) not in visited:
                            q.append((new_board, new_zero_pos))
                            visited.add(str(new_board))
                # print(q)
            moves += 1
        return -1

    def findZero(self, board, m, n):
        for i in range(m):
            for j in range(n):
                if board[i][j] == 0:
                    return (i, j)


board = [[4, 1, 2], [5, 0, 3]]
print('minMoves :', Solution().slidingPuzzle(board))
