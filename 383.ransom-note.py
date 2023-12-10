#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d_note = self.count_character(ransomNote)
        d_magazine = self.count_character(magazine)

        for character in d_note:
            if not (
                (character in d_magazine)
                and (d_note[character] <= d_magazine[character])
            ):
                return False

        return True

    def count_character(self, s: str) -> dict:
        d = {}
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        return d


# @lc code=end
