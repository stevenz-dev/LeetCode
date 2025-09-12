from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1
        
        while l < r:
            sum = numbers[l] + numbers[r]
            if sum == target:
                return [l+1, r+1]
            elif sum < target:
                l += 1
            else:
                r -= 1

# The tests are generated such that there is exactly one solution. You may not use the same element twice.
