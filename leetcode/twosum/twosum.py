from typing import List

class twosum:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)): # for i, num in enumerate(nums):
            complement = target - nums[i] # complement = target - num

            if complement in seen:
                return [i, seen[complement]]

            seen[nums[i]] = i # seen[num] = i