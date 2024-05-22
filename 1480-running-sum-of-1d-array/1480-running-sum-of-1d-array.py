class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum_list = []
        current_sum = 0
        for num in nums:
            current_sum += num
            sum_list.append(current_sum)
        return sum_list