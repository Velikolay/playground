from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        res = []
        min_len = min(len(el) for el in strs)
        for i in range(min_len):
            chars = {el[i] for el in strs}
            if len(chars) > 1:
                break
            res.append(strs[0][i])
        return "".join(res)
