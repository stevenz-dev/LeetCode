class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for i in range(len(nums)):
            dict[nums[i]] = i
        print(dict)

        for i in range(len(nums)):
            print(i, dict.get(target - nums[i]))
            if dict.get(target - nums[i]) and i != dict.get(target - nums[i]):
                return [i, dict.get(target - nums[i])]


solution = Solution()

nums = [3,4,3,6]
nums = [1,3,4,2]

print(solution.twoSum(nums, 6))
