class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_indexes = []
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_indexes.append(i)
                nums.append(0)
        for i in sorted(zero_indexes, reverse = True):
            nums.pop(i)