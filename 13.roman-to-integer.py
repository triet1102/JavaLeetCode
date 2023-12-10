#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        d = {
            "I": 1,
            "IV": 4,
            "V": 5,
            "IX": 9,
            "X": 10,
            "XL": 40,
            "L": 50,
            "XC": 90,
            "C": 100,
            "CD": 400,
            "D": 500,
            "CM": 900,
            "M": 1000,
        }
        total = 0
        index = 0
        len_s = len(s)
        while index + 1 < len_s:
            if s[index : index + 2] in d:
                total += d[s[index : index + 2]]
                index += 2
                print(f"index + 2 = {index}")
            else:
                total += d[s[index]]
                index += 1
                print(f"index + 1 = {index}")

        if index + 1 == len_s:
            total += d[s[index]]

        return total


# @lc code=end
