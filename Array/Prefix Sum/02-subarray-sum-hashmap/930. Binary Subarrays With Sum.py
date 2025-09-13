from typing import List
from collections import defaultdict

# Similar to 560. Subarray Sum Equals K
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        pre = 0
        cnt = defaultdict(int)
        cnt[0] = 1
        ans = 0
        for x in nums:
            pre += x
            ans += cnt[pre - goal]   # all past prefixes that make sum==goal
            cnt[pre] += 1            # store current prefix for future
        return ans