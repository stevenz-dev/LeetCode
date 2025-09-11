from typing import List

class Solution(object):
    # basketwangCoding
    # https://www.youtube.com/watch?v=eHtHNK3Lfmw
    # https://leetcode.com/problems/3sum-closest/discuss/8026/Python-solution-(two-pointer).
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        nums.sort()
        i = 0
        mindiff = sum(nums[:3]) - target
        while i < n-2:
            left = i+1
            right = n-1
            while left < right:
                diff = nums[i] + nums[left] + nums[right] - target
                if diff == 0: return target
                if abs(mindiff) > abs(diff): mindiff = diff
                if diff < 0:
                    left += 1
                else:
                    right -= 1
            i += 1

        return target + mindiff


    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # Sort to enable two-pointer search
        nums.sort()
        n = len(nums)

        # Initialize best_sum with any valid 3-number sum (first three after sort)
        best_sum = nums[0] + nums[1] + nums[2]

        for i in range(n - 2):
            # Optional micro-optimization: skip same nums[i] to reduce duplicate work
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, n - 1
            while left < right:
                current = nums[i] + nums[left] + nums[right]

                # Update best_sum if current is closer to target
                if abs(current - target) < abs(best_sum - target):
                    best_sum = current

                if current == target:
                    # Perfect match; cannot get closer than this
                    return target
                elif current < target:
                    # Need a larger sum; move left forward
                    left += 1
                    # Optional: skip duplicates to speed up (not required for correctness)
                    # while left < right and nums[left] == nums[left - 1]:
                    #     left += 1
                else:
                    # Need a smaller sum; move right backward
                    right -= 1
                    # Optional: skip duplicates to speed up
                    # while left < right and nums[right] == nums[right + 1]:
                    #     right -= 1

        return best_sum


"""
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.
Example:
Given array nums = [-1, 2, 1, -4], and target = 1.
The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""
solution = Solution()
nums = [-1, 2, 1, -4]
target = 1
print(solution.threeSumClosest(nums, target))