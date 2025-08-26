from typing import List
import collections

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # Flatten the 2x3 board into a string state
        start = "".join(str(x) for row in board for x in row)
        target = "123450"

        # Adjacency list for each index (0..5) indicating where '0' can swap with
        adj = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4]
        }

        def neighbors(state: str):
            """Generate all next states by swapping '0' with its adjacent indices."""
            res = []
            zero = state.index('0')
            for nxt in adj[zero]:
                s_list = list(state)
                # swap zero with the adjacent position
                s_list[zero], s_list[nxt] = s_list[nxt], s_list[zero]
                res.append("".join(s_list))
            return res

        # BFS
        queue = collections.deque([start])
        visited = {start}
        steps = 0

        while queue:
            size = len(queue)
            for _ in range(size):
                cur = queue.popleft()
                if cur == target:
                    return steps
                for nxt in neighbors(cur):
                    if nxt not in visited:
                        visited.add(nxt)
                        queue.append(nxt)
            steps += 1

        return -1

board = [[4, 1, 2], [5, 0, 3]]
print('minMoves :', Solution().slidingPuzzle(board))