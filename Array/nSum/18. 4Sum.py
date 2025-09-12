from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res: List[List[int]] = []

        for i in range(n-3):
            # Skip duplicate 'i'
            if i > 0 and nums[i] == nums[i-1]:
                continue

            # Pruning 1: smallest possible sum too large
            min_sum_i = nums[i] + nums[i+1] + nums[i+2] + nums[i+3]
            if min_sum_i > target:
                break  # further i only larger
            # Pruning 2: largest possible sum too small
            max_sum_i = nums[i] + nums[n-1] + nums[n-2] + nums[n-3]
            if max_sum_i < target:
                continue

            for j in range(i+1, n-2):
                # Skip duplicate 'j'
                if j > i+1 and nums[j] == nums[j-1]:
                    continue

                # Pruning 3: smallest possible sum at this (i,j)
                min_sum_j = nums[i] + nums[j] + nums[j+1] + nums[j+2]
                if min_sum_j > target:
                    break
                # Pruning 4: largest possible sum at this (i,j)
                max_sum_j = nums[i] + nums[j] + nums[n-1] + nums[n-2]
                if max_sum_j < target:
                    continue

                # Two-pointer on the tail segment
                left, right = j + 1, n - 1
                need = target - nums[i] - nums[j]

                while left < right:
                    s = nums[left] + nums[right]
                    if s == need:
                        res.append([nums[i], nums[j], nums[left], nums[right]])

                        # Skip duplicates for 'left'
                        lv = nums[left]
                        while left < right and nums[left] == lv:
                            left += 1

                        # Skip duplicates for 'right'
                        rv = nums[right]
                        while left < right and nums[right] == rv:
                            right -= 1

                    elif s < need:
                        left += 1
                    else:
                        right -= 1

        return res

# Example:
print(Solution().fourSum([1,0,-1,0,-2,2], 0))
# [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]