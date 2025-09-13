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


# Constraints:

# 1 <= trips.length <= 1000
# trips[i].length == 3
# 1 <= numPassengersi <= 100
# 0 <= fromi < toi <= 1000
# 1 <= capacity <= 105
class Solution(object):
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # solution 1
        stations = [0] * (max(trip[-1] for trip in trips) + 1)
        print(stations)

        for trip in trips:
            for i in range(trip[1], trip[2]):
                stations[i] += trip[0]
                if stations[i] > capacity: return False
        return True

        # solution 2
        # 最多有 1001 个车站
        nums = [0] * 1001
        df = Difference(nums)

        for trip in trips:
            val, start, end = trip
            df.increment(start, end-1, val)

        res = df.result()

        # 检查是否超载
        for i in range(len(res)):
            if capacity < res[i]:
                return False
        return True

trips = [[2, 1, 5], [3, 3, 7]]
capacity = 4
print(Solution().carPooling(trips, capacity))
