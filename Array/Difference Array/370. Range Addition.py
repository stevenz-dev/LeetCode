from pprint import pprint
# Assume you have an array of length n initialized with all 0's and are given k
# update operations.
#
# Each operation is represented as a triplet: [startIndex, endIndex, inc] which
# increments each element of subarray A[startIndex ... endIndex] (startIndex
# and endIndex inclusive) with inc.
#
# Return the modified array after all k operations were executed.
#
# Example:
#
#
# Input: length = 5, updates = [[1,3,2],[2,4,3],[0,2,-2]]
# Output: [-2,0,3,5,3]
#
#
# Explanation:
#
#
# Initial state:
# [0,0,0,0,0]
#
# After applying operation [1,3,2]:
# [0,2,2,2,0]
#
# After applying operation [2,4,3]:
# [0,2,5,5,3]
#
# After applying operation [0,2,-2]:
# [-2,0,3,5,3]

# You are given a list of update operations to apply to an array. The array is initially filled with zeros. The operations are represented by a 2D array, where each subarray has 3 elements: [startIndex, endIndex, increment]. The increment is to be applied to all elements from startIndex to endIndex (inclusive).


class Difference:
    def __init__(self, nums):
        self.diff = [0] * len(nums)
        self.diff[0] = nums[0]
        for i in range(1, len(nums)):
            self.diff[i] = nums[i] - nums[i-1]

    def increment(self, start, end, val):
        self.diff[start] += val
        # 当 j+1 >= diff.length 时，说明是对 nums[i] 及以后的整个数组都进行修改，那么就不需要再给 diff 数组减 val 了。
        if end + 1 < len(self.diff):
            self.diff[end + 1] -= val

    def result(self):
        res = [0] * len(self.diff)
        res[0] = self.diff[0]
        for i in range(1, len(self.diff)):
            res[i] = res[i-1] + self.diff[i]
        return res


class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        nums = [0] * length
        df = Difference(nums)
        print(f"nums: {nums}")
        print(f"diff: {df.diff}")

        for update in updates:
            start, end, val = update
            df.increment(start, end, val)

        return df.result()


length = 5
updates = [[1, 3, 2], [2, 4, 3], [0, 2, -2]]
print(Solution().getModifiedArray(length, updates))
# result: [-2, 0, 3, 5, 3]
