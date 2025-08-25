from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        path = []
        res = []

        def backtrack():
            if len(path) == len(nums):
                res.append(path[:])
                return

            for num in nums:
                if num in path:
                    continue
                path.append(num)
                backtrack()
                path.pop()

        backtrack()
        return res

nums = [1,2,3]
print(Solution().permute(nums))
# Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]