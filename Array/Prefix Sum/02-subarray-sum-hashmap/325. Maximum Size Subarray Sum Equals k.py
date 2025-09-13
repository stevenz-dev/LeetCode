from typing import List

class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        pre_sum = 0
        seen = {0: -1}   # 前缀和=0 在索引 -1 出现过
        max_len = 0

        for j, num in enumerate(nums):
            pre_sum += num

            if pre_sum - k in seen:
                max_len = max(max_len, j - seen[pre_sum - k])

            # 只记录第一次出现的位置
            if pre_sum not in seen:
                seen[pre_sum] = j

        return max_len

# 给定一个数组 nums 和一个整数 k，找到一个 和为 k 的最长子数组的长度。
# 返回这个长度，如果不存在这样的子数组，返回 0。