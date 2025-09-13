from pprint import pprint
from typing import List

class Difference:
    def __init__(self, nums):
        self.diff = [0] * len(nums)
        self.diff[0] = nums[0]
        for i in range(1, len(nums)):
            self.diff[i] = nums[i] - nums[i-1]

    def increment(self, start, end, val):
        self.diff[start] += val
        # 当 j+1 >= diff.length 时，说明是对 nums[i] 及以后的整个数组都进行修改，
        # 那么就不需要再给 diff 数组减 val 了。
        if end + 1 < len(self.diff):
            self.diff[end + 1] -= val

    def result(self):
        res = [0] * len(self.diff)
        res[0] = self.diff[0]
        for i in range(1, len(self.diff)):
            res[i] = res[i-1] + self.diff[i]
        return res


class Solution(object):
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        nums = [0] * n
        df = Difference(nums)

        for booking in bookings:
            start, end, val = booking
            df.increment(start-1, end-1, val)

        return df.result()


bookings = [[1,2,10],[2,3,20],[2,5,25]]
n = 5
print(Solution().corpFlightBookings(bookings, n))
