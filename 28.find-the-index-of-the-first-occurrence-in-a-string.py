#
# @lc app=leetcode id=28 lang=python3
#
# [28] Find the Index of the First Occurrence in a String
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h_len, n_len = len(haystack), len(needle)

        if h_len == n_len:
            return 0 if needle == haystack else -1

        for i in range(h_len - n_len + 1):
            if haystack[i : i + n_len] == needle:
                return i

        return -1


# @lc code=end
