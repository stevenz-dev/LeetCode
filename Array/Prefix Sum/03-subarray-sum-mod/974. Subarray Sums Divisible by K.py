from collections import defaultdict
from typing import List

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        cnt = defaultdict(int)
        cnt[0] = 1          # empty prefix
        pre = 0
        ans = 0
        for x in nums:
            pre += x
            mod = pre % k   # Python's % is non-negative even if pre is negative
            ans += cnt[mod]
            cnt[mod] += 1
        return ans
