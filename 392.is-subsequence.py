#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        idx_s = idx_t = 0
        while idx_s < len(s) and idx_t < len(t):
            if s[idx_s] == t[idx_t]:
                idx_s += 1
                idx_t += 1
            else:
                idx_t += 1

        return True if idx_s == len(s) else False


# @lc code=end
