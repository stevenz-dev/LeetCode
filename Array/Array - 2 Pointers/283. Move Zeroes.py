from typing import List

class Solution(object):
    # https://www.youtube.com/watch?v=rkV_no6QTFs
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                slow = i
                fast = i + 1
                while fast < n:
                    if nums[fast] != 0:
                        nums[slow], nums[fast] = nums[fast], nums[slow]
                        slow += 1
                    fast += 1
                return

        #        L
        #        ↓
        # [1, 3, 0, 0, 5, 0, 6]
        #              ↑
        #              R
        # two pointers
        # L always point to the first zero, R loops to the end.
        if len(nums) == 1: return

        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                l = i
                r = i + 1
                while r < n:
                    if nums[r] != 0:
                        nums[l], nums[r] = nums[r], nums[l]
                        l += 1
                    r += 1


    # https://www.youtube.com/watch?v=aayNRwUN3Do&ab_channel=NeetCode
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        for r in range(len(nums)):
            if nums[r]:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
        return nums


nums = [0,1,0,3,12]
Solution().moveZeroes(nums)
print(nums)
nums = [0]
Solution().moveZeroes(nums)
print(nums)
