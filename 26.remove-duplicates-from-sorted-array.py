#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 0
        len_nums = len(nums)
        for i in range(1, len_nums):
            if nums[i] != nums[index]:
                index += 1
                nums[index] = nums[i]

        return index + 1


# @lc code=end
