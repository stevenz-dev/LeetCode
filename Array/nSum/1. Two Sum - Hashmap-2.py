from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}  # Store number -> index
        for i, num in enumerate(nums):
            complement = target - num
            # Check if the complement is already in hashmap
            if complement in hashmap:
                return [hashmap[complement], i]
            # Store the current number with its index
            hashmap[num] = i
        return []


nums = [2,7,11,15]
print(Solution().twoSum(nums, 9))