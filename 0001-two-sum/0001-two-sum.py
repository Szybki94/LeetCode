class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}
        for i, j in enumerate(nums):
            complement = target - j
            if complement in num_to_index:
                return [num_to_index[complement], i]
            num_to_index[j] = i