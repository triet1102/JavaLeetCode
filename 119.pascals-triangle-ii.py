#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        else:
            previous_row = [1]
            for row_idx in range(1, rowIndex + 1):
                current_row = [1]
                for idx in range(1, row_idx):
                    current_row.append(previous_row[idx - 1] + previous_row[idx])
                current_row.append(1)
                previous_row = current_row

            return current_row


# @lc code=end
