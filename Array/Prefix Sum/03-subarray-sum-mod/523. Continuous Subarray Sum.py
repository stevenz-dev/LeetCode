from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        pre = 0
        first = {0: -1}  # remainder 0 first seen at index -1 (empty prefix)

        for j, x in enumerate(nums):
            pre += x
            mod = pre % k
            if mod in first:
                # ensure subarray length >= 2
                if j - first[mod] >= 2:
                    return True
            else:
                # store the earliest index for this remainder
                first[mod] = j
        return False
