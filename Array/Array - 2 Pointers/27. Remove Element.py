from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
        # print(nums)
        return slow


solution = Solution()
nums = [3,2,2,3]
print(solution.removeElement(nums, 3))
