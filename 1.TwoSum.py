class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) < 1:
            return False;
        buff_dict = {}
        for i, num in enumerate(nums):
            if nums[i] in buff_dict:
                return[buff_dict[num],i]
            else:
                buff_dict[target - num] = i