class Solution:
    def isValid(self, s: str) -> bool:
        paranthesis = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        stack = []
        for ch in s:
            if ch in {'(', '{', '['}:
                stack.append(ch)
            if ch in {')', '}', ']'}:
                if len(stack) > 0 and paranthesis[stack[-1]] == ch:
                    stack.pop()
                else:
                    return False
        return False if len(stack) > 0 else True


if __name__ == '__main__':
    print(Solution().isValid("()"))
