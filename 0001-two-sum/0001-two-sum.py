# Third solution with study case:
# Dicts AKA hashmaps!!!
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        for idx, value in enumerate(nums):
            sub_res = target - value
            if sub_res in dictionary:
                return [dictionary[sub_res], idx]
            dictionary[value] = idx
        
# This is O(n) solution
            