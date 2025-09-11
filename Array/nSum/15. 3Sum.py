from typing import List

class Solution:
    # basketwangCoding
    # https://www.youtube.com/watch?v=gq-uWp327m8&t=363s
    # https://leetcode.com/problems/3sum/discuss/7652/Python-solution-196ms
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        nums = sorted(nums)
        i = 0

        while i < n-2:
            left = i+1
            right = n-1

            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    right -= 1
                elif sum > 0:
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    right -= 1
                else:
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    left += 1

            while i < n-2 and nums[i] == nums[i+1]:
                i += 1
            i += 1
        return res


    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res: List[List[int]] = []

        for i in range(n):
            # Skip duplicate first elements
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # Two-pointer search for pairs summing to -nums[i]
            target = -nums[i]
            left, right = i + 1, n - 1

            while left < right:
                s = nums[left] + nums[right]
                if s == target:
                    res.append([nums[i], nums[left], nums[right]])
                    # Skip duplicates on the left
                    lv = nums[left]
                    while left < right and nums[left] == lv:
                        left += 1
                    # Skip duplicates on the right
                    rv = nums[right]
                    while left < right and nums[right] == rv:
                        right -= 1
                elif s < target:
                    left += 1
                else:
                    right -= 1

        return res


"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
Note:
The solution set must not contain duplicate triplets.

Example:
Given array nums = [-1, 0, 1, 2, -1, -4],
A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""
solution = Solution()
nums = [-1, 0, 1, 2, -1, -4]
print(nums)
print(solution.threeSum(nums))
