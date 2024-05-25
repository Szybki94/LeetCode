# Second thought solution
# There is no need to repeat going through the same number in every loop
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx_1, value_1 in enumerate(nums):
            for idx_2, value_2 in enumerate(nums[idx_1+1:], idx_1+1): # Here is added a little optimization
                if (value_1 + value_2) == target:
                    return [idx_1, idx_2]

# But is still O(n^2) solution :/
            