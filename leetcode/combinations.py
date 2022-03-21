def n_length_combo(lst, n):
    if n == 0:
        return [[]]

    combos = []
    for i in range(len(lst)):

        m = lst[i]
        rem_lst = lst[i + 1:]

        for p in n_length_combo(rem_lst, n - 1):
            combos.append([m] + p)

    return combos


if __name__ == "__main__":
    arr = "abc"
    print(n_length_combo([x for x in arr], 2))
