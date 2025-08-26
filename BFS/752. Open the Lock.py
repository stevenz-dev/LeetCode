from typing import Optional
from typing import List
import collections

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)
        queue = collections.deque(["0000"])
        visited = {"0000"}
        step = 0

        while queue:
            size = len(queue)
            # Expand all nodes in the current level of the queue
            for i in range(size):
                cur = queue.popleft()

                # Skip if the current node is a deadend
                if cur in dead:
                    continue
                # Found the target
                if cur == target:
                    return step

                # Generate all neighbor nodes by rotating one wheel
                for next in self.neighbors(cur):
                    if next not in visited:
                        visited.add(next)
                        queue.append(next)
            step += 1

        return -1

    def neighbors(self, node: str) -> List[str]:
        res = []
        for i in range(4):  # Four wheels
            digit = int(node[i])

            # Rotate one step upward
            up = (digit + 1) % 10
            res.append(node[:i] + str(up) + node[i+1:])

            # Rotate one step downward
            down = (digit + 9) % 10
            res.append(node[:i] + str(down) + node[i+1:])
        return res


deadends = ["0201", "0101", "0102", "1212", "2002"]
target = "0202"
print('minTurns :', Solution().openLock(deadends, target))
