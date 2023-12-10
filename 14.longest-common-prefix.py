#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        min_len = min(len(s) for s in strs)
        common = ""
        if min_len == 0:
            return common

        for i in range(min_len):
            if all(s[i] == strs[0][i] for s in strs[1:]):
                common += strs[0][i]
            else:
                return common

        return common


# @lc code=end
