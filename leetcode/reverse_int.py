class Solution:
    def reverse(self, x: int) -> int:
        sint = str(x)
        if len(sint) == 1:
            return x

        res = [""] * len(sint)
        start, end = 0, len(sint) - 1
        if sint[start] == "-":
            start += 1
            res[0] = "-"
        if sint[end] == "0":
            end -= 1

        while start <= end:
            res[start] = sint[end]
            res[end] = sint[start]
            start += 1
            end -= 1

        res = int("".join(res))
        return res if res in range(-2 ** 31, 2 ** 31 - 1) else 0