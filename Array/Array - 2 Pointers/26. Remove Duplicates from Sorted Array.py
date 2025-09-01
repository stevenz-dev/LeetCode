from typing import List


class Solution(object):
    # https://www.youtube.com/watch?v=WVfNtGL7ROM
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = 1
        for fast in range(1, len(nums)):
            if nums[fast - 1] != nums[fast]:
                nums[slow] = nums[fast]
                slow += 1
        return slow

    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        slow = 0  # Position of last unique element
        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
        return slow + 1


solution = Solution()
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(solution.removeDuplicates(nums))
