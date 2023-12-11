#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}

        for i in range(len(s)):
            if s[i] not in s_dict:
                s_dict[s[i]] = i

            if t[i] not in t_dict:
                t_dict[t[i]] = i

            if s_dict[s[i]] != t_dict[t[i]]:
                return False

        return True


# @lc code=end
