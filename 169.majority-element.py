#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # len_major = int(len(nums) / 2)
        # d = {}
        # for num in nums:
        #     if num in d:
        #         d[num] += 1
        #     else:
        #         d[num] = 1

        #     if d[num] > len_major:
        #         return num

        index, count = 0, 1
        for i in range(1, len(nums)):
            if nums[i] == nums[index]:
                count += 1
            else:
                count -= 1

            if count == 0:
                index = i
                count = 1

        return nums[index]


# @lc code=end
