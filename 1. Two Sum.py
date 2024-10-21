class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        final_list = {}
        for index, value in enumerate(nums):
            num_2 = target - value
            if num_2 in final_list:
                return [final_list[num_2], index]
            final_list[value] = index

        return []