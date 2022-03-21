import sys
from typing import List


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target, window = {}, {}
        valid = 0
        left, right = 0, 0
        start, length = left, sys.maxsize

        for ch in t:
            target[ch] = target.get(ch, 0) + 1

        while right < len(s):
            ch = s[right]
            right += 1
            if ch in target:
                window[ch] = window.get(ch, 0) + 1
                if window[ch] == target[ch]:
                    valid += 1

            while valid == len(target):
                if right - left < length:
                    length = right - left
                    start = left

                ch = s[left]
                left += 1
                if ch in target:
                    window[ch] -= 1
                    if window[ch] < target[ch]:
                        valid -= 1

        if length == sys.maxsize:
            return ""
        else:
            return s[start: start + length]

    # def minWindow(self, s: str, t: str) -> str:
    #     char_pos = {ch: [] for ch in t}
    #     for idx in range(len(s)):
    #         ch = s[idx]
    #         if ch in char_pos:
    #             char_pos[ch].append(idx)
    #
    #     char_pos = list(char_pos.values())
    #     groups = self.calcGroups(char_pos, len(char_pos))
    #     windows = [(min(group), max(group)) for group in groups]
    #
    #     min_size = windows[0][1] - windows[0][0]
    #     min_win = windows[0]
    #     for win in windows:
    #         size = win[1] - win[0]
    #         if size < min_size:
    #             min_size = size
    #             min_win = win
    #
    #     return s[min_win[0]: min_win[1] + 1]
    #
    # def calcGroups(self, items, k) -> List[List[int]]:
    #     if k == 0:
    #         return [[]]
    #
    #     idx = len(items) - k
    #     res = []
    #     prev_win = self.calcGroups(items, k - 1)
    #     for item in items[idx]:
    #         for win in prev_win:
    #             res.append([item] + win)
    #     return res


if __name__ == "__main__":
    print(Solution().minWindow("ADOBECODEBANC", "ABC"))
