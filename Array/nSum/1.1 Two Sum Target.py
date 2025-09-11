from typing import List

def twoSumTarget(nums: List[int], target: int) -> List[List[int]]:
    res = []
    nums.sort()  # Sort to handle duplicates
    left, right = 0, len(nums) - 1

    while left < right:
        s = nums[left] + nums[right]
        if s == target:
            res.append([nums[left], nums[right]])
            # Skip duplicates on the left
            while left < right and nums[left] == nums[left + 1]:
                left += 1
            # Skip duplicates on the right
            while left < right and nums[right] == nums[right - 1]:
                right -= 1
            left += 1
            right -= 1
        elif s < target:
            left += 1
        else:
            right -= 1

    return res


# Example
print(twoSumTarget([1, 3, 1, 2, 2, 3], 4))
# Output: [[1, 3], [2, 2]]