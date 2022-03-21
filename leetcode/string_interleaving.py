from functools import cache


class Solution:

    @cache
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if not any([s1, s2, s3]):
            return True

        if len(s1) + len(s2) != len(s3):
            return False

        res = False
        if s1 and s3 and s1[0] == s3[0]:
            res |= self.isInterleave(s1[1:], s2, s3[1:])

        if s2 and s3 and s2[0] == s3[0]:
            res |= self.isInterleave(s1, s2[1:], s3[1:])

        return res
