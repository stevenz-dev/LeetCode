from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        # build prefix sum array
        self.prefix = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.prefix[i + 1] = self.prefix[i] + nums[i]
        print(self.prefix)

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]


# init: O(n)
# sumRange: O(1)
# Space: O(n)

# Your NumArray object will be instantiated and called as such:
nums = [-2, 0, 3, -5, 2, -1]
obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
param_1 = obj.sumRange(0, 2)
# return (-2) + 0 + 3 = 1
print(param_1)
param_2 = obj.sumRange(2, 5)
# return 3 + (-5) + 2 + (-1) = -1
print(param_2)
param_3 = obj.sumRange(0, 5)
# return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3
print(param_3)
