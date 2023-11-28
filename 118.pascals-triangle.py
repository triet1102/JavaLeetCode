#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        else:
            res = [[1]]
            for row_idx in range(1, numRows):
                row_previous_vals = res[row_idx - 1]
                row_current_vals = [1]
                for idx in range(1, row_idx):
                    row_current_vals.append(
                        row_previous_vals[idx - 1] + row_previous_vals[idx]
                    )
                row_current_vals.append(1)

                res.append(row_current_vals)

            return res


# @lc code=end
