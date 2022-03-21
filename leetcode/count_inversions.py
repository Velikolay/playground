def countInversions(arr):
    # Write your code here
    _, inv = countInversionsRec(arr)
    return inv


def countInversionsRec(arr):
    # Write your code here
    if len(arr) < 2:
        return arr, 0

    mid = len(arr) // 2
    arr1, inv1 = countInversionsRec(arr[:mid])
    arr2, inv2 = countInversionsRec(arr[mid:])
    res, inv = merge(arr1, arr2)
    return res, inv1 + inv2 + inv


def merge(arr1, arr2):
    res = []
    inversions = 0
    i1, i2 = 0, 0
    while i1 < len(arr1) and i2 < len(arr2):
        if arr1[i1] <= arr2[i2]:
            res.append(arr1[i1])
            i1 += 1
        else:
            res.append(arr2[i2])
            i2 += 1
            inversions += len(arr1) - i1

    res.extend(arr1[i1:])
    res.extend(arr2[i2:])

    return res, inversions


if __name__ == "__main__":
    # print(merge([1, 5, 7], [0, 3, 10]))
    print(countInversions([2, 1, 3, 1, 2]))
    # print(countInversionsRec([3, 2, 1]))

