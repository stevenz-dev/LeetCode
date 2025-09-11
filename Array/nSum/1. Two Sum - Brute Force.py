from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Iterate through all pairs (i, j)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                # Check if the pair adds up to target
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

# Time: O(n^2)
# Space: O(1)

nums = [2, 7, 11, 15]
print(Solution().twoSum(nums, 9))
