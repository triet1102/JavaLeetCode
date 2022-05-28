#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        la = len(a)
        lb = len(b)
        res = ""
        if la < lb:
            a = "0" * (lb -la) + a
        else:
            b = "0" * (la - lb) + b

        mem = 0
        for i in reversed(range(len(a))):
            sum = int(a[i]) + int(b[i]) + mem
            res = str(sum%2) + res
            mem = sum // 2
        
        if mem == 1:
            res = "1" + res

        return res

# @lc code=end

