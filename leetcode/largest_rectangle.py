def largestRectangle(h):
    area = 0
    stack = [[h[0], 0]]
    for i in range(1, len(h)):
        if h[i] > h[i-1]:
            stack.append([h[i], i])
        else:
            b = None
            while stack and h[i] < stack[-1][0]:
                b = stack.pop()
                area = max(area, b[0] * (i - b[1]))    # Calc the max area before i
            stack.append([h[i], b[1] if b else i])

    for b in stack:
        area = max(area, b[0]*(stack[-1][1] - b[1] + 1))
    return area


if __name__ == "__main__":
    print(largestRectangle([1, 2, 3, 4, 5]))
