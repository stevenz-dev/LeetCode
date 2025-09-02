from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)

        slow = 1  # Position of last kept element
        for fast in range(2, len(nums)):
            # Compare current number with nums[slow-1]
            if nums[fast] != nums[slow - 1]:
                slow += 1
                nums[slow] = nums[fast]

        return slow + 1

nums = [0,0,1,1,1,1,2,3,3]
print(Solution().removeDuplicates(nums))