from typing import List
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        count[0] = 1  # base case: 前缀和本身等于 k
        res = 0
        pre_sum = 0

        for num in nums:
            pre_sum += num
            res += count[pre_sum - k]
            count[pre_sum] += 1
            print(pre_sum)
        print(count)

        return res


nums = [1,1,1]
k = 2
print(Solution().subarraySum(nums, k))