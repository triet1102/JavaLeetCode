#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        is_continue = False
        count = 0
        for c in s:
            if c != " ":
                if is_continue:
                    count += 1
                else:
                    is_continue = True
                    count = 1
            else:
                is_continue = False

        return count


# @lc code=end
