def binsearch(cost, i, j, el):
    if i > j:
        return -1

    el_idx = (i + (j - i) // 2)
    if el == cost[el_idx]:
        return el_idx

    if el < cost[el_idx]:
        return binsearch(cost, i, el_idx - 1, el)
    else:
        return binsearch(cost, el_idx + 1, j, el)


def binarySearchIter(cost, left, right, target):
    while left <= right:
        mid = left - (right - left) // 2
        if cost[mid] == target:
            return mid
        elif target > cost[mid]:
            left = mid + 1
        elif target < cost[mid]:
            right = mid - 1
    return -1


def whatFlavors(cost, money):
    sorted_cost = sorted(cost)
    # print(sorted_cost)
    for i in range(len(sorted_cost) - 1):
        j = binsearch(sorted_cost, i + 1, len(cost) - 1, money - sorted_cost[i])
        if j != -1:
            fi, fj = -1, -1
            # print(i, j)
            for ri in range(len(cost)):
                if fi == -1 and cost[ri] == sorted_cost[i]:
                    fi = ri
                    continue

                if fj == - 1 and cost[ri] == sorted_cost[j]:
                    fj = ri
                    continue
            print(" ".join(map(str, sorted([fi + 1, fj + 1]))))
            return


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())

        n = int(input())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)
# if __name__ == "__main__":
#     whatFlavors([7, 2, 5, 4, 11], 12)
