from typing import List

def kSum(nums: List[int], target: int, k: int) -> List[List[int]]:
    nums.sort()
    return kSumHelper(nums, target, k, 0)

def kSumHelper(nums: List[int], target: int, k: int, start: int) -> List[List[int]]:
    res = []
    n = len(nums)

    # Base case: 2Sum with two pointers
    if k == 2:
        left, right = start, n - 1
        while left < right:
            s = nums[left] + nums[right]
            if s == target:
                res.append([nums[left], nums[right]])
                lv, rv = nums[left], nums[right]
                # Skip duplicates
                while left < right and nums[left] == lv:
                    left += 1
                while left < right and nums[right] == rv:
                    right -= 1
            elif s < target:
                left += 1
            else:
                right -= 1
        return res

    # General case: reduce kSum to (k-1)Sum
    for i in range(start, n - k + 1):
        # Avoid duplicates
        if i > start and nums[i] == nums[i - 1]:
            continue
        # Early pruning
        if nums[i] * k > target:  # too large
            break
        if nums[-1] * k < target:  # too small
            continue

        # Recursively solve (k-1)Sum
        for subset in kSumHelper(nums, target - nums[i], k - 1, i + 1):
            res.append([nums[i]] + subset)

    return res


print(kSum([1,3,1,2,2,3], 4, 2))
# Output: [[1, 3], [2, 2]]

print(kSum([-1,0,1,2,-1,-4], 0, 3))
# Output: [[-1, -1, 2], [-1, 0, 1]]

print(kSum([1,0,-1,0,-2,2], 0, 4))
# Output: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
