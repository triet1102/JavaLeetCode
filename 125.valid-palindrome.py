#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_processed = "".join([c.lower() for c in s if c.isalnum()])
        len_s_processed = len(s_processed)
        for i in range(len_s_processed // 2):
            if s_processed[i] != s_processed[len_s_processed - i - 1]:
                return False

        return True


# @lc code=end
