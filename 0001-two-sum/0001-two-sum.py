# First thought solution
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx_1, value_1 in enumerate(nums):
            for idx_2, value_2 in enumerate(nums):
                if idx_1 == idx_2:
                    continue
                elif (value_1 + value_2) == target:
                    return [idx_1, idx_2]
            