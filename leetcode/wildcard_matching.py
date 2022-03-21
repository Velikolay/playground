class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return self.isMatchRec(s, p, 0, 0)

    def isMatchRec(self, s: str, p: str, s_idx: int, p_idx: int) -> bool:
        if p_idx == len(p) and s_idx == len(s):
            return True
        if p_idx == len(p) and s_idx < len(s):
            return False

        if s_idx < len(s) and (s[s_idx] == p[p_idx] or p[p_idx] == "?"):
            return self.isMatchRec(s, p, s_idx + 1, p_idx + 1)

        if p[p_idx] == "*":
            return self.isMatchRec(s, p, s_idx, p_idx + 1) or (s_idx < len(s) and self.isMatchRec(s, p, s_idx + 1, p_idx + 1)) or (s_idx < len(s) and self.isMatchRec(s, p, s_idx + 1, p_idx))
        return False
