#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        l, h = 0, x

        while l <= h:
            mid = (l + h) // 2
            if mid * mid <= x < (mid + 1) * (mid + 1):
                return mid
            elif mid * mid > x:
                h = mid - 1
            else:
                l = mid + 1
        

                
# @lc code=end

