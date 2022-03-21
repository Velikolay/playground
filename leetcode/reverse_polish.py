from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = {"+", "-", "*", "/"}
        stack = []
        for token in tokens:
            if token not in operands:
                stack.append(token)
            else:
                o2 = stack.pop()
                o1 = stack.pop()
                if token == "/":
                    stack.append(str(int(int(o1) / int(o2))))
                else:
                    stack.append(str(eval(o1 + token + o2)))
        return int(stack.pop())


if __name__ == "__main__":
    print(Solution().evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
