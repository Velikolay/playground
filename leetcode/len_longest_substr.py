class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ch_dict = {}
        start, curr, seq_len = 0, 0, 0
        while curr < len(s):
            ch = s[curr]
            if ch in ch_dict:
                prev = ch_dict[ch]
                if prev >= start:
                    if curr - start > seq_len:
                        seq_len = curr - start

                    start = prev + 1

            ch_dict[ch] = curr

            curr += 1

        if curr - start > seq_len:
            seq_len = curr - start

        return seq_len


if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring("abcabcbb"))
